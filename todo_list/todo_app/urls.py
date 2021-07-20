#todo app view

from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('', views.todo_view, name="todo_app-todo_view"),
    path('add_item/', views.add_item),
    path('remove_item/<int:todo_id>/', views.remove_item)
]