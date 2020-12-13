from django.urls import path
from .views import RegisterUser

app_name = "accounts"

from . import views

urlpatterns = [
    path('begin', views.begin, name='begin'),
    #path('add_user', views.add_user, name='add_user'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('password_change', views.password_change, name='password_change'),
]
