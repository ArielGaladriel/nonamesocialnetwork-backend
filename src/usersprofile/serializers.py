from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import UsersProfile, UsersBio
from django.contrib.auth.password_validation import validate_password


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


class ProfileCreationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=UsersProfile.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UsersProfile
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = UsersProfile.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user