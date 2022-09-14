from django.db import models
from django.conf import settings


class Follower(models.Model):
    """
    Relation between owner and subscribers
    """
    STATUS = (
        ('requested', 'requested'),
        ('confirmed', 'confirmed')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers')
    status = models.CharField(max_length=20, choices=STATUS)
