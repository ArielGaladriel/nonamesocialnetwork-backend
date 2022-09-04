from rest_framework import serializers
from .models import Follower
from src.usersprofile.models import UsersProfile


class SubscribersSerializer(serializers.ModelSerializer):
    """
    """
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UsersProfile
        fields = ['id', 'username', 'avatar']


class FollowersListSerializer(serializers.ModelSerializer):
    """
    """
    subscribers = SubscribersSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ['subscribers']