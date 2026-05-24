
from django.contrib import admin
from django.urls import path
from core.views import home, CategoriaList, CategoriaCreate, CategoriaUpdate, CategoriaDetail, CategoriaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name= "home"),
    path('categorias/', CategoriaList.as_view(), name="categorias"),
    path('categorias/create/', CategoriaCreate.as_view(), name="categorias_create"),
    path('categorias/update/<int:pk>', CategoriaUpdate.as_view(), name="categorias_update"),
    path('categorias/detail/<int:pk>', CategoriaDetail.as_view(), name="categorias_detail"),
    path('categorias/delete/<int:pk>', CategoriaDelete.as_view(), name="categorias_delete"),
]