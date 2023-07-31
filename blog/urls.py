from django.urls import path
from. import views
urlpatterns = [
    path('',views.home_page, name='home'),
    path('create-blog/', views.createBlog, name='create'),
    
    path('sign-up/', views.sign_user, name='sign-up'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login' ),
    
    
    path('post/<str:pk>/', views.getblog, name='blog'),
]