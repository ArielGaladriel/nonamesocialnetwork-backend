from rest_framework import serializers

from .models import UsersPost


class PostSerializer(serializers.ModelSerializer):
    """
    """

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UsersPost
        fields = '__all__'


class PostsListSerializer(serializers.ModelSerializer):
    """Looks exactly as PostSerializer, but I guess I'll change smth here in the future
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UsersPost
        fields = ['id','user', 'label', 'text', 'creation_date']