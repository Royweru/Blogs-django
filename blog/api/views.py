from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from rest_framework import status
from .serializers import BlogSerializer
@api_view(['GET','POST'])
def getBlogs(request):
    if request.method == 'GET':
        blogs  = Post.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PATCH','PUT','DELETE','GET'])        
def blog_details(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'PUT':
        serializer = BlogSerializer(post,request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = BlogSerializer(post)
        return Response(serializer.data)