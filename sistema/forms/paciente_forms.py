from django import forms
from sistema.models import Paciente

class PacienteForm(forms.ModelForm):
    cpf = forms.CharField(
        max_length=14,
        label='CPF',
    )
    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf',]
        # criacao_data e ativo não aparecem: são preenchidos automatiamente.
        labels = {
            'nome' : 'Nome',
            'sobrenome' : 'Sobrenome',
            'email' : 'E-mail',
            'telefone' : 'Telefone',
            'cpf' : 'CPF',
        }