from rest_framework import serializers

from .models import UsersPost


class PostSerializer(serializers.ModelSerializer):
    '''
    '''

    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = UsersPost
        fields = '__all__'


class PostsListSerializer(serializers.ModelSerializer):
    """
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UsersPost
        fields = ['user', 'label', 'text', 'creation_date']