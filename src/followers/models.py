from django.db import models
from django.conf import settings


class Follower(models.Model):
    """ Relation between owner and subscribers
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers')
    allowed_permissions = models.CharField(max_length=20, blank=True)
