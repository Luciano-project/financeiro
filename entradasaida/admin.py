from django.contrib import admin
from .models import Receita
# Register your models here.
class ListaEntradaouSaida(admin.ModelAdmin):
    list_display = ('receita')

    def __str__(self):
        return "Entradas e Saídas"
admin.site.register(Receita)
