from django.urls import path
from api.views import usuario_role

urlpatterns = [
    path("usuarioRole/", usuario_role.UsuarioRoleListDetailView.as_view(), name="usuario_role-list"),
    path("usuarioRole/<int:pk>/", usuario_role.UsuarioRoleDetailView.as_view(), name="usuario_role-detail"),
    path("usuarioRole/criar/", usuario_role.UsuarioRoleCreateView.as_view(), name="usuario_role-create"),
    path("usuarioRole/atualizar/<int:pk>/", usuario_role.UsuarioRoleUpdateView.as_view(), name="usuario_role-update"),
]
