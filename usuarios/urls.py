from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    #path('cadastro/', views.cadastro_item, name='cadastro'),
    path('logout', views.logout, name='logout'),
    #path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    #path('registro', views.registro_item, name='registro_item'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    path('novo_usuario', views.novo_usuario, name='novo_usuario'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('alterar_senha', views.alterar_senha, name='alterar_senha'),
]

