from django.urls import path
from . import views

urlpatterns = [
    path('state/', views.state, name='state'),
    path('grid/', views.viewState, name='view-state'),
    path('info/<str:pk>/', views.infoLocation, name='info'),
    path('add/', views.addLocation, name='add-location'),
    path('list_items/', views.list_items, name='listy'),
    path('add_items/', views.add_items, name='addy'),
    path('update_items/<str:pk>/', views.update_items, name='update'),
    path('delete_items/<str:pk>/', views.delete_items, name='delete'),
]