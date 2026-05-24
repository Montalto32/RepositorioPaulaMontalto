
from django.urls import path
from producto.views import (
    CategoriaList,
    CategoriaCreate,
    CategoriaUpdate,
    CategoriaDetail,
    CategoriaDelete,
)

urlpatterns = [
    path("", CategoriaList.as_view(), name="categorias"),
    path("create/", CategoriaCreate.as_view(), name="categoria_create"),
    path("update/<int:pk>/", CategoriaUpdate.as_view(), name="categoria_update"),
    path("detail/<int:pk>/", CategoriaDetail.as_view(), name="categoria_detail"),
    path("delete/<int:pk>/", CategoriaDelete.as_view(), name="categoria_delete"),
]