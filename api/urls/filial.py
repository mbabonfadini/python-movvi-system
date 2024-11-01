from django.urls import path
from api.views import filial

urlpatterns = [
    path('filiais/', filial.FilialListView.as_view(), name='filial-list'),
    path('filiais/<int:pk>/', filial.FilialDetailView.as_view(), name='filial-detail'),
    path('filiais/criar/', filial.FilialCreateView.as_view(), name='filial-create'),
    path('filiais/atualizar/<int:pk>/', filial.FilialUpdateView.as_view(), name='filiai-update'),
]
