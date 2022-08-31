from rest_framework import serializers
from .models import UsersProfile, UsersBio


class ProfileSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = UsersProfile
        fields = ['id', 'first_name', 'last_name', 'birthday']


class BioSerializer(serializers.ModelSerializer):
    """Public information about user
    """

    class Meta:
        model = UsersBio
        fields = '__all__'


