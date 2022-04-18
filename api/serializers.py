from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Target


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TargetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True)
    user_id = serializers.StringRelatedField()

    class Meta:
        model = Target
        fields = (
            'user_id',
            'id',
            'target1_1',
            'target1_2',
            'target1_3',
            'target1_4',
            'target1_5',
            'target1_6',
            'target1_7',
            'target1_8',
            'target1_9',
            'target2_1',
            'target2_2',
            'target2_3',
            'target2_4',
            'target2_5',
            'target2_6',
            'target2_7',
            'target2_8',
            'target2_9',
            'target3_1',
            'target3_2',
            'target3_3',
            'target3_4',
            'target3_5',
            'target3_6',
            'target3_7',
            'target3_8',
            'target3_9',
            'target4_1',
            'target4_2',
            'target4_3',
            'target4_4',
            'target4_5',
            'target4_6',
            'target4_7',
            'target4_8',
            'target4_9',
            'target5_1',
            'target5_2',
            'target5_3',
            'target5_4',
            'target5_5',
            'target5_6',
            'target5_7',
            'target5_8',
            'target5_9',
            'target6_1',
            'target6_2',
            'target6_3',
            'target6_4',
            'target6_5',
            'target6_6',
            'target6_7',
            'target6_8',
            'target6_9',
            'target7_1',
            'target7_2',
            'target7_3',
            'target7_4',
            'target7_5',
            'target7_6',
            'target7_7',
            'target7_8',
            'target7_9',
            'target8_1',
            'target8_2',
            'target8_3',
            'target8_4',
            'target8_5',
            'target8_6',
            'target8_7',
            'target8_8',
            'target8_9',
            'target9_1',
            'target9_2',
            'target9_3',
            'target9_4',
            'target9_5',
            'target9_6',
            'target9_7',
            'target9_8',
            'target9_9',
            'created_at',
        )
