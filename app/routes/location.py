from django.urls import path
from app.views.location import (
    create_location, 
    list_locations, 
    update_location, 
    delete_location, 
)

urlpatterns = [
    path('cadastrar/local/', create_location, name='create-location'),
    path('atualizar/local/<int:pk>/', update_location, name='update-location'),
    path('deletar/local/<int:pk>/', delete_location, name='delete-location'),
    path('listar/locais/', list_locations, name='list-locations'),
]