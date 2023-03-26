from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('create/', PostList.as_view()),
    path('create/<int:id>/', PostDetail.as_view()),
    path('all/', PostList.as_view()),
]
