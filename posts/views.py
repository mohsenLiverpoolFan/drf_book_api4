from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer
# Create your views here.
from .models import Post
from rest_framework.response import Response
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


class PostList(generics.ListAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
