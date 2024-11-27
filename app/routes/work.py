from django.urls import path

from app.views.work import (
    create_work, 
    list_works, 
    update_work, 
    delete_work, 
    works_done
)

urlpatterns = [
    path('obras-feitas/', works_done, name='works-done'),
    path('cadastrar/obra/', create_work, name='create-work'),
    path('atualizar/obra/<int:pk>/', update_work, name='update-work'),
    path('deletar/obra/<int:pk>/', delete_work, name='delete-work'),
    path('listar/obras/', list_works, name='list-works'),
]