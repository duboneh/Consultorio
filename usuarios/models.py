from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=14, null=True, blank=True, verbose_name='CPF', help_text="Digite somente os números.")
    celular = models.CharField(max_length=16, null=True, blank=True, help_text="Digite somente os números.")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
