from rest_framework import serializers
from .models import UsersProfile, UsersBio


class BioSerializer(serializers.ModelSerializer):
    """Public information about user
    """
    class Meta:
        model = UsersBio
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    """
    """
    bio = BioSerializer

    class Meta:
        model = UsersProfile
        fields = ['id','first_name','last_name','birthday','bio']
        depth = 1
