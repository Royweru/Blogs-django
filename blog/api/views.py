from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import BlogSerializer
@api_view(['GET'])
def getBlogs(request):
    blogs  = Post.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)