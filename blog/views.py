from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer, UserSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(slug=slugify(serializer.validated_data['name']))


class AuthorList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdminAuthorsList(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super(PostList, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class AdminDestroyPostView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
