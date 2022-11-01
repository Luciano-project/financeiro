"""financeiro URL Configuratlogoution

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuario/', include('usuarios.urls')),
    path('registro-item/', views.registro_item, name='registro_item'),
    path('editar-item/<int:id>/', views.editar_item, name='editar_item'),
    path('deleta/<int:item_id>', views.deleta_item, name='deleta'),
    #path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
]
