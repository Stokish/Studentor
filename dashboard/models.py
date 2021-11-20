from random import sample
import string
from django.db import models
from django.contrib.auth.models import User


class CourseKeywords(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CourseDirection(models.Model):
    name = models.CharField(max_length=100)
    keywords = models.ManyToManyField(CourseKeywords)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Course(models.Model):
    LESSON_TYPES = (
        ('1', 'Mono'),
        ('2', 'Regular')
    )
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.ForeignKey(CourseDirection, on_delete=models.CASCADE)
    image = models.ImageField(default='clip-reading-books.png', upload_to='course_pics')
    lesson_cost = models.IntegerField()
    date_lesson = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    duration = models.CharField(max_length=20)
    lesson_type = models.CharField(max_length=100, choices=LESSON_TYPES, default='1')
    lesson_url = models.URLField(max_length=200)
    max_student = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_author')
    students = models.ManyToManyField(User, related_name='applied_students', blank=True)
    key = models.TextField(blank=True, null=True)
    report_by_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        super(Course, self).save()
        self.key = self.course_name + self.author.username + str(self.lesson_cost) + self.subject.name
        self.key = ''.join(sample(self.key, k=len(self.key)))
        self.key += str(self.pk)
        self.key =self.key.translate({ord(c): None for c in string.whitespace})
        super(Course, self).save()

    def __str__(self):
        return self.course_name
