from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create-post', CreateBlogPost.as_view(), name="create-post"),
    path('update-post/<int:pk>', UpdateBlogPost.as_view(), name="update-post"),
    path('detail-post/<int:pk>', DetailBlogPost.as_view(), name="detail-post"),
    path('delete-post/<int:pk>', DeleteBlogPost.as_view(), name="delete-post"),
]