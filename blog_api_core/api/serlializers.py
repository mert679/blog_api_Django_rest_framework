from django.db.models import fields
from rest_framework import serializers
from .models import Blogs
  
class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = fields = ['title', 'author', 'body']