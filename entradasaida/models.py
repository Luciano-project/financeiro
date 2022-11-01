from django.db import models

# Create your models here.
class Receita(models.Model):
    receita_despesa = models.CharField(max_length=50)

    def __str__(self):
        return self.receita_despesa
