from django.db import models


class Produtos(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.IntegerField('Preço')
    estoque = models.IntegerField('Quantidade em estoque')


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('Email', max_length=100)