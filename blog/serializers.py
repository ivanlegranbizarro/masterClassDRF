from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
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
        fields = ['title', 'content', 'author', 'files']
        read_only_fields = ['author']

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        from_email = settings.EMAIL_HOST_USER
        to_email = [post.author.email]
        send_mail(
            'Post Created',
            'Your post has been created',
            from_email,
            to_email,
            fail_silently=False
        )

        return post


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'email': {'required': True}
        }
