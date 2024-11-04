from django.urls import path
from api.views import role

urlpatterns = [
    path("roles/", role.RoleListView.as_view(), name="role-list"),
    path("role/<int:pk>/", role.RoleDetailView.as_view(), name="role-detail"),
    path("role/criar/", role.RoleCreateView.as_view(), name="role-create"),
    path("role/atualizar/<int:pk>/", role.RoleUpdateView.as_view(), name="role-update"),
]
