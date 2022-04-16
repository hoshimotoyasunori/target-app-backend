from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Large, Middle, Task


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LargeSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Large
        fields = (
            'id',
            'large',
            'created_at'
        )

class MiddleSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    target_large = serializers.StringRelatedField()
    class Meta:
        model = Middle
        fields = (
            'id',
            'target_large',
            'middle',
            'created_at'
        )

class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    target_middle = serializers.StringRelatedField()
    class Meta:
        model = Task
        fields = (
            'id',
            'target_middle',
            'task',
            'created_at'
        )
