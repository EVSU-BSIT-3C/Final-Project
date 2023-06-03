from django.urls import path
from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('addTodo/', views.addTodo, name='addTodo'),
    path('addCategory/', views.addCategory, name='addCategory'),
    path('<int:todo_id>/edit/', views.edit, name='edit'),
    path('<int:todo_id>/update/', views.update, name='update'),
    path('<int:todo_id>/delete/', views.delete, name='delete'),
]
