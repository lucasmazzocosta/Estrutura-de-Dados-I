from django.db import models # ORM do Django para declarar modelos no BD.
from django.utils import timezone # Útil para gerar data/hora atual do projeto.

# Modelo que representa um Paciente.
# atributos => nome, sobrenome, email, telefone, data de cadastro, mensagem, ativo(True/False).
class Paciente(models.Model):
    nome = models.CharField(max_length=25) # Nome do paciente
    sobrenome = models.CharField(max_length=50) # Sobrenome do paciente
    email = models.EmailField() # Email de contato do paciente
    telefone = models.CharField(max_length=20) # Telefone de contato
    criacao_data = models.DateTimeField(default=timezone.now) #Data/hora cadastro
    mensagem = models.TextField(blank=True) # Campo opcional livre para mensagem
    ativo = models.BooleanField(default=True) #  