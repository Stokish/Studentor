from random import sample
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Course


@receiver(post_save, sender=Course)
def create_course(sender, instance, created, **kwargs):
    if created:
        instance.key = instance.course_name + instance.author.username + str(instance.lesson_cost) + instance.subject.name
        instance.key = ''.join(sample(instance.key, k=len(instance.key)))
        instance.key += str(instance.pk)
