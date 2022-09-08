from rest_framework import serializers
from .models import Follower
from ..usersprofile.models import UsersProfile


class UsersNameSerializer(serializers.ModelSerializer):
    """
    Username and avatar of follower, that will be displayed in "followers list" page
    """
    gender = serializers.ReadOnlyField(source='bio.gender')  # switch to 'bio.avatar' later

    class Meta:
        model = UsersProfile
        fields = ['username','gender']


class FollowersListSerializer(serializers.ModelSerializer):
    """
    List of user's followers
    """
    subscriber = UsersNameSerializer()

    class Meta:
        model = Follower
        fields = ['subscriber']