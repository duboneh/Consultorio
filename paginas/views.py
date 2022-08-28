from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    #Classe filha do TemplateView precisa do atributo abaixo para definir um template a ser renderizado
    template_name = "paginas/index.html"

class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'