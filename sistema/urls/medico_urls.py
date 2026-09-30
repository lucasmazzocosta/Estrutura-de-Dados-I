from django.urls import path
from sistema.views import medico_view

url_patterns = [
    path('medico/', medico_view), # vollmed.com/medico
    path('medico/novo/'), # vollmed.com/medico/novo
    path('medico/perfil/<int:medico_id>'), # vollmed.com/medico/perfil/<int:medico_id>
    path('medico/listagem'), # vollmed.com/medico/listagem
]