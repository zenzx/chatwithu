from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('<str:room_name>/', views.room, name='room')
]