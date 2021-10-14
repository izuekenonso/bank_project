from django.conf.urls import url
from django.urls import path, include
from .views import UserApiView, UserDetailApiView
from .views import TransactionApiView, TransactionDetailApiView


urlpatterns = [
    path('user/', UserApiView.as_view()),
    path('user/<int:user_id>/', UserDetailApiView.as_view()),
    path('transaction/', TransactionApiView.as_view()),
    path('transaction/<int:user_id>/', TransactionApiView.as_view())
]