from django import forms
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=10,unique=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=FEMALE,
    )

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'