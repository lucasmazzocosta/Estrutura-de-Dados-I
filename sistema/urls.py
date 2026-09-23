from django.contrib import admin
from django.urls import path

from sistema.views import medico_view

url_patterns = [
    path('medico/', medico_view),
]