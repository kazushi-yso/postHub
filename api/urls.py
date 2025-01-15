from django.urls import path
from .views import HelloAPIView
from .views import UserAPIView
from .views import PostAPIView

urlpatterns = [
    path('hello/', HelloAPIView.as_view(), name='hello'),
    path('user/', UserAPIView.as_view(), name='register'),
    path('post/', PostAPIView.as_view(), name='register'),
    path('post/<int:id>/', PostAPIView.as_view(), name='delete_post'),















]
