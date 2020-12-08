from django.urls import path
from .views import RegisterUser

app_name = "accounts"

from . import views

urlpatterns = [
    path('begin', views.begin, name='begin'),
    path('add_user', views.add_user, name='add_user'),
    path('register/', RegisterUser.as_view(), name='register'),
]
