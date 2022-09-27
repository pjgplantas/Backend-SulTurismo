from django.db import models


class Formulario(models.Model):
    nome = models.CharField(max_length=255)
    cepdestino = models.CharField(max_length=9)
    ceporigem = models.CharField(max_length=9)
    qtd = models.IntegerField()
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome
