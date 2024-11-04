from django.urls import path
from api.views import cargo

urlpatterns = [
    path('cargos/', cargo.CargoListView.as_view(), name='cargo-list'),
    path('cargo/<int:pk>/', cargo.CargoDetailView.as_view(), name='cargo-detail'),
    path('cargo/criar/', cargo.CargoCreateView.as_view(), name='cargo-create'),
    path('cargo/atualizar/<int:pk>/', cargo.CargoUpdateView.as_view(), name='cargo-update'),
]
