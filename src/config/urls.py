
from django.contrib import admin
from django.urls import path
from core.views import saludar , saludar_con_etiqueta, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path('saludar/', saludar),
    path("saludar2", saludar_con_etiqueta)
    ]

