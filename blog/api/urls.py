from django.urls import path
from . import views

urlpatterns = [
    path('', views.getBlogs),
    path('<str:pk>/',views.blog_details)
    
]
