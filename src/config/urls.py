
from django.contrib import admin
from django.urls import path
from core.views import home, CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= "home"),
    path('categorias/', CategoriaList.as_view(), name="categorias"),
    path('categorias/create', CategoriaCreate.as_view(), name="categorias"),
    path('categorias/update/<int:pk>', CategoriaUpdate.as_view(), name="categorias"),
    path('categorias/detail/<int:pk>', CategoriaDetail.as_view(), name="categorias"),
]