from django.http.response import HttpResponse
from django.shortcuts import render
from .models import cep_big_users, Post


def views_cep(request):
    list_uf = cep_big_users.objects.all()

    data = {
        'ceps': list_uf,
        }

    return render(request, 'index.html', data)

def views_post(request):
    data = {
        'posts' : Post.Rua,
    }

    return render(request, 'index.html', data)

