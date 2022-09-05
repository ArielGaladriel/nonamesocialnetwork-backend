from rest_framework import serializers
from .models import Follower
from ..usersprofile.models import UsersProfile


class UsersNameSerializer(serializers.ModelSerializer):
    """
    """
    gender = serializers.ReadOnlyField(source='bio.gender')  # switch to 'bio.avatar' later

    class Meta:
        model = UsersProfile
        fields = ['username','gender']


class FollowersListSerializer(serializers.ModelSerializer):
    """
    """
    subscriber = UsersNameSerializer()

    class Meta:
        model = Follower
        fields = ['subscriber']