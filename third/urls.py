from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name = 'list'),
    path('list/<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='restaurant-create'),
    path('delete/<int:id>',views.delete, name = 'restaurant-delete'),
    path('update/', views.update, name = 'restaurant-update'),
]