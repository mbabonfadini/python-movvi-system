from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from ..models import SolicitacaoTipo
from ..serializers import SolicitacaoTipoSerializer
from ..utils import AuthenticatedView



class SolicitacaoTipoListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = SolicitacaoTipoSerializer

    def get_queryset(self):
        return get_list_or_404(SolicitacaoTipo)



class SolicitacaoTipoDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = SolicitacaoTipo
    serializer_class = SolicitacaoTipoSerializer

    def get_object(self):
        solicitacao_tipo_id: int = self.kwargs.get('pk')

        return get_object_or_404(SolicitacaoTipo, pk=solicitacao_tipo_id)



class SolicitacaoTipoCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class = SolicitacaoTipoSerializer



class SolicitacaoTipoUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = SolicitacaoTipo
    serializer_class = SolicitacaoTipoSerializer



    def patch(self, request, *args, **kwargs):
        partial: bool = True
        return self.update(request, *args, partial= partial, **kwargs)



    def update(self, request, *args, **kwargs):
        partial: bool = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)