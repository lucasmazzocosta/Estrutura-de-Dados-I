from django.http import HttpResponse
from django.shortcuts import render

# Views - retornam algo, são funções, request -> response
# View responsável pela tela inicial da consulta
def consulta_view(request):
    print('Página consulta funcionou')
    return HttpResponse('Página inicial da consulta')