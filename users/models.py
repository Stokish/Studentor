from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500)
    university = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    website = models.URLField(max_length=200)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    USER_ROLES = (
        ('student', 'Student'),
        ('mentor', 'Mentor')
    )
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other')
    )
    user_role = models.CharField(max_length=10, choices=USER_ROLES)

    gender = models.CharField(max_length=10, choices=GENDER)
    date_of_birth = models.DateField()
    strong_at = models.TextField()
    hobbies = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
