from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post_method/', views.post_method, name='post_method'),
]