from django.urls import path

app_name = "accounts"

from . import views

urlpatterns = [
    path('begin', views.begin, name='begin'),
]
