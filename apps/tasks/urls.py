from django.urls import path

from . import views

app_name = "tasks"



urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
]
