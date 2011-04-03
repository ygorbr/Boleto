from django.db import models

class Fatura (models.Model):
    Nome = models.CharField(max_length=50)
    Cartao = models.CharField(max_length=150)
    Numero_Cartao = models.CharField(max_length=19)
    Fatura_Total = models.FloatField()
    Fatura_Minima = models.FloatField()
    Vencimento = models.DateField()


