from django.http import HttpResponse
from django.shortcuts import render

# Views - retornam algo, são funções, request -> response
# View responsável pela tela inicial do médico
def medico_view(request):
    print('Página médico funcionou')
    return HttpResponse('Página inicial do médico')