from django.db import models


class Post(models.Model):
        Acesso = models.CharField(max_length=60)
        CPF = models.CharField(max_length=14)
        dMail = models.CharField(max_length=100)
        Pais = models.CharField(max_length=7)
        CEP = models.CharField(max_length=14)
        Estado = models.CharField(max_length=2)
        Cidade = models.CharField(max_length=13)    
        Rua = models.CharField(max_length=100)
        Número = models.CharField(max_length=5)
        Complemento = models.CharField(max_length=50)

class cep_big_users(models.Model):
        Nome = models.CharField(max_length=100)
        CEP = models.CharField(max_length=8)
        Uf = models.CharField(max_length=2)
        Cidade = models.CharField(max_length=100)
        Bairro = models.CharField(max_length=100)
        Tipo_logradouro = models.CharField(max_length=30)
        Rua = models.CharField(max_length=100)
        Numeros = models.CharField(max_length=50)


