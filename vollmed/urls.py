
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_view),
]

# wwww.vollmed.online/
# wwww.vollmed.online/login
# wwww.vollmed.online/

# Medico
# www.vollmed.online/medico/id/ - Perfil do médico
# www.vollmed.online/medico/id/alterar - Alterar cadastro do médico

# www.vollmed.online/medico/id/consultas - Consultas do médico

# Paciente
# www.vollmed.online/Paciente/id/ - Perfil do Paciente
# www.vollmed.online/Paciente/id/alterar - Alterar cadastro do Paciente

# www.vollmed.online/Paciente/id/consultas/cadastrar
# www.vollmed.online/Paciente/id/consultas/alterar/id/ - ver, alterar e excluir consultas do Paciente

# Consulta
