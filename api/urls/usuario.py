from django.urls import path
from api.views import  usuarios, login


urlpatterns = [
    path('usuarios/', usuarios.UsuarioListView.as_view(), name='usuario-list'),
    path('usuario/<int:pk>/', usuarios.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuario/criar/', usuarios.UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuario/atualizar/<int:pk>/', usuarios.UsuarioUpdateView.as_view(), name='usuario-update'),
    path('login/', login.LoginView.as_view(), name='usuario-login'),
]