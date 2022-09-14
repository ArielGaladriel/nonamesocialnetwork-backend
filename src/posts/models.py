from django.db import models
from django.conf import settings


class UsersPost(models.Model):
    """
    Model for user's posts
    """
    PRIVACY = (
        ('public', 'public'),
        ('followers only', 'followers only'),
        ('best friends only', 'best friends only'),
        ('private', 'private')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    label = models.CharField(max_length=30)
    text = models.TextField(max_length=1024)
    creation_date = models.DateTimeField(auto_now_add=True)
    privacy = models.CharField(max_length=20, choices=PRIVACY, default='public')



