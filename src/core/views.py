from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from core.models import Categoria
from core.forms import CategoriaForm

def home(request):
    return render(request, "core/index.html")

class CategoriaList(ListView):
    model = Categoria 
    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = Categoria.objects.filter(nombre__contains= consulta)
        else:
            queryset = Categoria.objects.all()
        return queryset
                        
   
class CategoriaCreate (CreateView): 
    model = Categoria 
    form_class = CategoriaForm
    success_url = "/categorias/"
   # template_name = "core/categoria_form.html"

class CategoriaUpdate(UpdateView):
    model = Categoria 
    form_class = CategoriaForm
    success_url = "/categorias/"

class CategoriaDetail(DetailView):
    model = Categoria 

class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = "/categorias/"