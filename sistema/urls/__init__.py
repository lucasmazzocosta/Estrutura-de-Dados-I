from .paciente_urls import url_patterns as paciente_urlpatterns
from .medico_urls import url_patterns as medico_urlpatterns
from .consulta_urls import url_patterns as consulta_urlpatterns

url_patterns = paciente_urlpatterns + medico_urlpatterns + consulta_urlpatterns