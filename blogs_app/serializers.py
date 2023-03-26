from rest_framework import serializers
from .models import Blog

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at')
