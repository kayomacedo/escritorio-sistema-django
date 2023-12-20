from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('novo_documento/',views.novo_documento,name='novo_documento'),
    path('meus_documentos/', views.meus_documentos, name='meus_documentos'),
    path('excluir_documento/<int:documento_id>/', views.excluir_documento, name='excluir_documento'),
    path('pesquisar_documentos/', views.pesquisar_documentos, name='pesquisar_documentos'),
    path('relatorio/', views.relatorio, name='relatorio_documentos'),

]
