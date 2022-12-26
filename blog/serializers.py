from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Category, Post


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['slug']


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'email': {'required': True}
        }
