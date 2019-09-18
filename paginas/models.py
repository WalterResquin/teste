from django.db import models

# Create your models here.
class Produto(models.Model):
    codigo = models.CharField(max_length=30)
    nome = models.CharField(max_length=60)
    preco = models.DecimalField(max_digits=10, decimal_places=5, null=True)

    def __str__(self):
        return self.codigo[:20]


class Orcamento(models.Model):
    cod_orcamento = models.IntegerField()
    data = models.DateField()
    status = models.IntegerField(null = True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    #def __str__(self):
    #   return self.cod_orcamento[:20]

class ItemOrcamento(models.Model):
    cod_item = models.IntegerField()
    cod_item_orcamento = models.IntegerField()
    cod_produto = models.IntegerField()
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
