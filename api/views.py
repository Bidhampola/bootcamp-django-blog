from django.shortcuts import render

from rest_framework.decorators import api_view
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post,many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT','DELETE','GET'])
def post_details(request, id):
    post = get_object_or_404(Post,pk=id)

    if request.method == 'PUT':
        serializer = PostSerializer(post,data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response({'res':'Item deleted'})


