from rest_framework import serializers
from .models import Training, Content
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TrainingSerializer(serializers.ModelSerializer):
    # created_at = serializers.DateTimeField(format="%Y/%m/%d")

    class Meta:
        model = Training
        fields = ('id', 'review', 'evaluation', 'place', 'created_at', 'body_weight_10', 'updated_at')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'created_at', 'training_type', 'weight', 'set1', 'set2', 'set3')
