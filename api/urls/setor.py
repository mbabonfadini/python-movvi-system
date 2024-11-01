from django.urls import path
from api.views import setor

urlpatterns = [
    path('setor/', setor.SetorListView.as_view(), name='setor-list'),
    path('setor/<int:pk>/', setor.SetorDetailView.as_view(), name='setor-detail'),
    path('setor/criar/', setor.SetorCreateView.as_view(), name='setor-create'),
    path('setor/atualizar/<int:pk>/', setor.SetorUpdateView.as_view(), name='setor-update'),
]
