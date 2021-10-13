from django.conf.urls import url
from django.urls import path, include
from .views import UserApiView, UserDetailApiView


urlpatterns = [
    path('', UserApiView.as_view()),
    path('<int:user_id>/', UserDetailApiView.as_view())
]