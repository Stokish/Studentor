from django.db import models
from django.contrib.auth.models import User


class courseKeywords(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class courseDirection(models.Model):
    name = models.CharField(max_length=100)
    keywords = models.ManyToManyField(courseKeywords)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class courses(models.Model):
    LESSON_TYPES = (
        ('1', 'Mono'),
        ('2', 'Regular')
    )
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.ForeignKey(courseDirection, on_delete=models.CASCADE)
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
    students = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applied_students', null=True)

    def __str__(self):
        return self.course_name
