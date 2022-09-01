from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, PerfilUpdate, PasswordUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
            template_name='usuarios/login.html'
        ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    path('atualizar-perfil/', PerfilUpdate.as_view(), name='atualizar-perfil'),
    # path('atualizar-senha/', auth_views.PasswordChangeView.as_view(
    #         template_name='usuarios/alterar-senha.html'
    # ), name='atualizar-senha'),
    path('atualizar-senha/', PasswordUpdate.as_view(), name='atualizar-senha'),
]