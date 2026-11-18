from django.db import models # ORM do Django para declarar modelos no BD.
from django.utils import timezone # Útil para gerar data/hora atual do projeto.

# modelo que representa um Médico
class Medico(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    criacao_data = models.DateTimeField(default=timezone.now)
    telefone = models.CharField()
    crm = models.CharField(max_length=6)
    especialidade = models.CharField()
    mensagem = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"