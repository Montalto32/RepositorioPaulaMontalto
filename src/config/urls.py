
from django.contrib import admin
from django.urls import path
from core.views import home, CategoriaList, CategoriaCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= "home"),
    path('categorias/', CategoriaList.as_view(), name="categorias"),
    path('categorias/create', CategoriaCreate.as_view(), name="categorias"),
]