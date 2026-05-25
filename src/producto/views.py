from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)
from producto.models import Categoria
from producto.forms import CategoriaForm


class CategoriaList(ListView):
    model = Categoria
    template_name = "producto/categoria_list.html"
    context_object_name = "categorias"

    def get_queryset(self):
        consulta = self.request.GET.get("consulta")
        if consulta:
            return Categoria.objects.filter(nombre__icontains=consulta)
        return Categoria.objects.all()
                        
   
class CategoriaCreate (CreateView): 
    model = Categoria 
    form_class = CategoriaForm
    success_url = reverse_lazy('producto:categoria_home')
   # template_name = "core/categoria_form.html"

class CategoriaUpdate(UpdateView):
    model = Categoria 
    form_class = CategoriaForm
    success_url = reverse_lazy('producto:categoria_home')

class CategoriaDetail(DetailView):
    model = Categoria 

class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy('producto:categoria_home')
