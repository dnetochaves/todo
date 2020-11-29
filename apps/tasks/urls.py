from django.urls import path

from . import views

app_name = "tasks"



urlpatterns = [
    path('add_category/', views.add_category, name='add_category'),
    path('list_category/', views.list_category, name='list_category'),
    path('edit_category/<int:id_category>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:id_category>/', views.delete_category, name='delete_category'),
    path('add_task/', views.add_task, name='add_task'),
    path('list_task/', views.list_task, name='list_task'),
    path('edit_task/<int:id_task>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:id_task>/', views.delete_task, name='delete_task'),
]
