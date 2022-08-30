from django.db import models
from django.conf import settings


class UsersPost(models.Model):
    """Model for user's posts
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    label = models.CharField(max_length=30)
    text = models.TextField(max_length=1024)
    creation_date = models.DateTimeField(auto_now_add=True)
    allowed_permissions = models.CharField(max_length=20, blank=True)



