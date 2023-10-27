from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('aluno/<int:id>', detalhes, name='aluno_details'),
    path('aluno/<int:id>/edit', editar, name='aluno_edit'),
    path('aluno/criar', criar, name='aluno_new'),
    path('aluno/<int:id>/delete', deletar, name='aluno_delete'),
]