from django.db import models
from entradasaida.models import Receita
from datetime import datetime
from django.contrib.auth.models import User

class ControleFinanceiro(models.Model):
    receita_despesa = models.ForeignKey(Receita, on_delete=models.DO_NOTHING)
    categoria = models.CharField(max_length=200,null=True,blank=True)
    valor = models.FloatField()
    descricao = models.CharField(max_length=100)
    data_registro = models.DateField(default=datetime.now, blank=True)
    usuario = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        ordering = ['-data_registro']
