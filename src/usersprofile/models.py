from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class UsersProfile(AbstractUser):
    """ Custom user model
    """
    first_login = models.DateTimeField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)


class UsersBio(models.Model):
    """ Additional information about user
    """
    GENDER = (
        ('unknown', '----'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary'),
        ('other', 'Other')
    )

    user = models.OneToOneField(UsersProfile, on_delete=models.CASCADE, related_name='bio')
    gender = models.CharField(max_length=20, choices=GENDER, default='unknown')
    phone = models.CharField(max_length=14, blank=True)
    web_link = models.CharField(max_length=100, blank=True)
    about = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(blank=True, null=True)