from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
@api_view(['GET'])
def getBlogs(request):
    blogs  = Post.objects.all()
    return Response(blogs)