from django.db import models


class Task(models.Model):
    title = models.CharField('Дисциплина вопроса', max_length=50)
    task = models.TextField('Ваш вопрос')


class Mentor(models.Model):
    name = models.CharField('Имя и фамилия', max_length=50)
    email = models.EmailField('Ваша почта')
    telephone = models.CharField('Ваш номер телефона', max_length=20)
    university = models.CharField('Ваш Университет', max_length=50)
    discipline = models.CharField('Дисциплина, в котором нуждаетесь в менторе', max_length=50)


def __str__(self):
    return self.title
