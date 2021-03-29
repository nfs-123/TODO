from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.home),
    path('tasks', views.task),
    path('delete/<int:id>', views.delete,name='deletedata'),
    path('update/<int:id>', views.update, name='updatedata'),

]