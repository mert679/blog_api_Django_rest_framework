from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blogs
from .serlializers import BlogsSerializer
from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/blog/pk/delete',
        'detail_information': '/detail/pk'
    }
  
    return Response(api_urls)

@api_view(["POST"])

def add_blog(request):
    blog = BlogsSerializer(data=request.data)

    if Blogs.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    
    if blog.is_valid():
        blog.save()
        return Response(blog.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])

def list_blog(request):
    blog = Blogs.objects.all()
    serializer = BlogsSerializer(blog,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def update_blog(request,pk):
    blog = Blogs.objects.get(pk=pk)
    data = BlogsSerializer(instance = blog, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["DELETE"])

def delete_blog(request,pk):
    blog = get_object_or_404(Blogs,pk=pk)
    blog.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(["GET"])

def get_detail(request,pk):
    blog = get_object_or_404(Blogs,pk=pk)
    serializer = BlogsSerializer(blog)

    return Response(serializer.data)

