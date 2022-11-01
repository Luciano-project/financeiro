from django.contrib import admin
from .models import ControleFinanceiro
# Register your models here.

class ListandoControle(admin.ModelAdmin):
    list_display = ('id','descricao','data_registro','receita_despesa','usuario')
    #list_filter = ('categoria',)
    list_display_links = ['descricao']
    list_per_page = 10


admin.site.register(ControleFinanceiro,ListandoControle)

