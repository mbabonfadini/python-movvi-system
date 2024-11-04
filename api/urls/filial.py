from django.urls import path
from api.views import filial

urlpatterns = [
    path('filiais/', filial.FilialListView.as_view(), name='filial-list'),
    path('filial/<int:pk>/', filial.FilialDetailView.as_view(), name='filial-detail'),
    path('filial/criar/', filial.FilialCreateView.as_view(), name='filial-create'),
    path('filial/atualizar/<int:pk>/', filial.FilialUpdateView.as_view(), name='filiai-update'),
]
