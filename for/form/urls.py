from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('qabul/', views.qabul, name='qabul'),
    path('post/', views.qabul, name='post'),

]