from django.urls import path
from api.views import tipo_operacao_frete as tof

urlpatterns = [
    path("tipoOpFrete/", tof.TipoOperacaoFreteListView.as_view(), name="tof-list"),
    path("tipoOpFrete/<int:pk>/", tof.TipoOperacaoFreteDetailView.as_view(), name="tof-detail"),
    path("tipoOpFrete/criar/", tof.TipoOperacaoFreteCreateView.as_view(), name="tof-create"),
    path("tipoOpFrete/atualizar/<int:pk>/", tof.TipoOperacaoFreteUpdateView.as_view(), name="tof-update"),
]
