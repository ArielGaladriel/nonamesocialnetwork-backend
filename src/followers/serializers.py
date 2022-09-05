from rest_framework import serializers
from .models import Follower
from ..usersprofile.models import UsersProfile


class UsersNameSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = UsersProfile
        fields = ['id','username']


class FollowersListSerializer(serializers.ModelSerializer):
    """
    """
    subscriber = UsersNameSerializer()

    class Meta:
        model = Follower
        fields = ['subscriber']