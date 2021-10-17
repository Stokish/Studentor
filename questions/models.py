from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    subject = models.CharField(max_length=100)
    question = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Вопросы', blank=True, null=True,
                             related_name='comments_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор ответа', blank=True, null=True)
    create_date = models.DateTimeField(auto_now=True)
    text = models.TextField(verbose_name='Ответ к вопросу')
    status = models.BooleanField(verbose_name='Видимость ответа', default=False)
    likes = models.ManyToManyField(User, blank=True, related_name='comments_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comments_dislikes')
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    @property
    def children(self):
        return Comments.objects.filter(parent=self).order_by('create_date').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
