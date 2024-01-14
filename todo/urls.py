from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('<int:pk>/', views.TodoDetail.as_view(), name='todo-detail')
]
