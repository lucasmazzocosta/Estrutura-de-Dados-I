from django.urls import path
from sistema.views import consulta_view

url_patterns = [
    path('consulta/', consulta_view),  # vollmed.com/consulta
]