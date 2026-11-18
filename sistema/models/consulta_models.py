from django.db import models # ORM do Django para declarar modelos no BD.
from django.utils import timezone

from sistema.models import medico_models, paciente_models # Útil para gerar data/hora atual do projeto.

# modelo que representa uma consulta
#id, id do paciente, id do medico, horario/data, obs, status
class Consulta(models.Model):
    paciente_id = models.ForeignKey(paciente_models.Paciente, on_delete=models.CASCADE) # Chave estrangeira
    medico_id = models.ForeignKey(medico_models.Medico, on_delete=models.CASCADE) # Chave estrangeira
    data_consulta = models.DateTimeField(default=timezone.now) # Data/hora consulta
    ativa = models.BooleanField(default=True) # Campo de exclusão lógica
    observacao = models.TextField(blank=True) # Anotacao adicional
    status = models.CharField(
        default="A",
        max_length=1,
        choices=[
            ("A", "Agendada"),
            ("X", "Cancelada"),
            ("C", "Confirmada"),
            ("R", "Realizada"),
        ]
    )