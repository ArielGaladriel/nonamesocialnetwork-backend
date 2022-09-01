from rest_framework import serializers
from .models import UsersProfile, UsersBio


class BioSerializer(serializers.ModelSerializer):
    """Public information about user
    """
    class Meta:
        model = UsersBio
        exclude = ['id','user']


class SettingsSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = UsersProfile
        fields = ['first_name','last_name','email','birthday','password']


class ProfileSerializer(serializers.ModelSerializer):
    """
    """
    bio = BioSerializer

    class Meta:
        model = UsersProfile
        fields = ['id','first_name','last_name','birthday','bio']
        depth = 1
