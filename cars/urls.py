from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('create/', views.car_create, name='car_create'),
    path('<int:pk>/', views.car_detail, name='car_detail'),
    path('<int:pk>/update/', views.car_update, name='car_update'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
]