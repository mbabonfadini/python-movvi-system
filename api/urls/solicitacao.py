from django.urls import path
from api.views import solicitacao

urlpatterns = [
    path("solicitacao/", solicitacao.SolicitacaoListView.as_view(), name="solicitacao-list"),
    path("solicitacao/<int:pk>/", solicitacao.SolicitacaoDetailView.as_view(), name="solicitacao-detail"),
    path("solicitacao/criar/", solicitacao.SolicitacaoCreateView.as_view(), name="solicitacao-create"),
    path("solicitacao/atualizar/<int:pk>/", solicitacao.SolicitacaoUpdateView.as_view(), name="solicitacao-update"),
]
