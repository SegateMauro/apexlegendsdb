from django.db import models


country_choices = (
    ('brasil','Brasil'),
    ('eua', 'EUA'),
    ('uruguai','Uruguai'),
)

uf_choices = (
    ('AC','Acre'),
    ('AL','Alagoas'),
    ('AP','Amapá'),
    ('AM','Amazonas'),
    ('BA','Bahia'),
    ('CE','Ceará'),
    ('DF','Distrito Fedral'),
    ('MG','Minas Gerais'),
    ('PR','Paraná'),
    ('SP','São Paulo'),
)

city_choices = (
    ('americana', 'Americana'),
    ('araraquara', 'Araraquara'),
    ('belohorizonte','Belo Horizonte'),
    ('curitiba', 'Curitiba'),
)

class Home(models.Model):
    Pais = models.CharField(max_length=50, choices=country_choices, default='brasil')
    Estado = models.CharField(max_length=50, choices=uf_choices, default='SP')
    Cidade = models.CharField(max_length=50, choices=city_choices, default='SP')
    CEP = models.CharField(max_length=14)
    Rua = models.CharField(max_length=100)
    Número = models.CharField(max_length=5)
    Complemento = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title =models.CharField(max_length=200)
    content = models.TextField()