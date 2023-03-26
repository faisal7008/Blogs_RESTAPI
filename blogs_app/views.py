from rest_framework import generics
from .models import Blog
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
