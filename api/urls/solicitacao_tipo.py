from django.urls import path
from api.views import solicitacao_tipo as st



urlpatterns = [
    path("solicitacaoTipo/",  st.SolicitacaoTipoListView.as_view(), name="st-list"),
    path("solicitacaoTipo/<int:pk>/",  st.SolicitacaoTipoDetailView.as_view(), name="st-detail"),
    path("solicitacaoTipo/criar/",  st.SolicitacaoTipoCreateView.as_view(), name="st-create"),
    path("solicitacaoTipo/atualizar/<int:pk>/",  st.SolicitacaoTipoUpdateView.as_view(), name="st-update"),
]
