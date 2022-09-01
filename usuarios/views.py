from audioop import reverse
from multiprocessing import context
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "usuarios/registro.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    # Método executado para criar o objeto e salvar os dados no banco
    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="PowerUsers")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Novo Usuário"

        return context

#Classe para Update dos dados do Usuário

class PerfilUpdate(UpdateView):
    template_name = "usuarios/registro.html"
    model = Perfil
    fields = ['nome_completo', 'cpf', 'celular']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Meus dados"

        return context