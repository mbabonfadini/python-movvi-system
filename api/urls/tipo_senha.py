from django.urls import path
from api.views import tipo_senha

urlpatterns = [
    path("tipoSenha/", tipo_senha.TipoSenhaListView.as_view(), name="tipo_senha-list"),
    path("tipoSenha/<int:pk>/", tipo_senha.TipoSenhaDetailView.as_view(), name="tipo_senha-detail"),
    path("tipoSenha/criar/", tipo_senha.TipoSenhaCreateView.as_view(), name="tipo_senha-list"),
    path("tipoSenha/atualizar/<int:pk>/", tipo_senha.TipoSenhaUpdateView.as_view(), name="tipo_senha-list"),
]
