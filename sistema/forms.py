from django import forms
from sistema.models import *

# Checagem de e-mail - > O EmailField do model já valida se é e-mail válido.
# Checagem do dado inserido -> Dependendo do Field do atributo.

ESPECIALIDADES = [
    ('CARDIOLOGIA', "Cardiologia"),
    ('DERMATOLOGIA', 'Dermatologia'),
    ('GINECOLOGIA', 'Ginecologia'),
    ('NEUROLOGIA', 'Neurologia'),
    ('OFTALMOLOGIA', 'Oftalmologia'),
    ('ORTOPEDIA', 'Ortopedia'),
    ('PEDIATRIA', 'Pediatria'),
]

# Formulário do Médico (usado para cadastro e edição)
class MedicoForm(forms.ModelForm):
    # Troca o Charfield padrão por um <select> com opções fixas
    especialidade = forms.ChoiceField(
        choices = [('', 'Selecione uma especialidade')] + ESPECIALIDADES,
        label='Especialidade',
    )

    class Meta:
        model = Medico
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'crm', 'especialidade']
        # criacao_data e ativo não aparecem: são preenchidos automatiamente.
        labels = {
            'nome' : 'Nome',
            'sobrenome' : 'Sobrenome',
            'email' : 'E-mail',
            'telefone' : 'Telefone',
            'crm' : 'CRM',
        }