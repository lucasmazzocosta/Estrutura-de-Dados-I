# from django.http import HttpResponse
from django.shortcuts import render
from sistema.models import Paciente

# Views - retornam algo, são funções, request -> response
# View responsável pela tela inicial do paciente
def index(request):
    return render(
        request, 
        'global/base.html',
        )

# View responsável por listar todos os pacientes
def listar_pacientes(request):
    pacientes = Paciente.objects.all() # -> [objeto1, objeto2, objeto3]

    context = {
        'pacientes': pacientes
    }

    return render(
        request,
        'paciente/listar.html',
        context,
    )

