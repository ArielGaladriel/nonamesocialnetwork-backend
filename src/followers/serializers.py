from rest_framework import serializers
from .models import Follower


class FollowersListSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Follower
        fields = ['subscriber']