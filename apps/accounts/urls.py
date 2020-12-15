from django.urls import path
from .views import RegisterUser

app_name = "accounts"

from . import views

urlpatterns = [
    path('begin', views.begin, name='begin'),
    path('add_user', views.add_user, name='add_user'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('password_change', views.password_change, name='password_change'),
    path('', views.add_user_profile, name='add_user_profile'),
    path('list_user_profile', views.list_user_profile, name='list_user_profile'),
    path('change_user_profile/<username>/', views.change_user_profile, name='change_user_profile'),
    path('change_user_information/<username>/', views.change_user_information, name='change_user_information'),
]
