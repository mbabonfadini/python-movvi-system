from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from ..models import Solicitacao
from ..serializers import SolicitacaoSerializer
from ..utils import AuthenticatedView, CustomPagination



class SolicitacaoListView(generics.ListAPIView):
    serializer_class = SolicitacaoSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
        
        usuario_id = self.request.query_params.get('usuario')
        tipo_solicitacao_id = self.request.query_params.get('tipo')
        status_id = self.request.query_params.get('status')

        filters = {}    

        if usuario_id:
            filters['usuario'] = usuario_id
        if tipo_solicitacao_id:
            filters['tipo_solicitacao'] = tipo_solicitacao_id
        if status_id:
            filters['status'] = status_id
        
        if not filters:
            return Solicitacao.objects.none()
        
        return get_list_or_404(Solicitacao, **filters)



class SolicitacaoDetailView(generics.RetrieveAPIView):
    queryset = Solicitacao
    serializer_class = SolicitacaoSerializer

    def get_object(self, value):
        solicitacao_id: int = self.kwargs.get('pk')

        return get_object_or_404(Solicitacao, pk=solicitacao_id)
    


class SolicitacaoCreateView(generics.CreateAPIView):
    serializer_class = SolicitacaoSerializer



class SolicitacaoUpdateView(generics.UpdateAPIView):
    queryset = Solicitacao
    serializer_class = SolicitacaoSerializer

    def patch(self, request, *args, **kwargs):
        partial: bool = True
        return self.update(request, *args, partial=partial, **kwargs)

    

    def update(self, request, *args, **kwargs):
        partial: bool = kwargs.pop('partial', False)
        instance= self.get_object()
        serializer = self.get_serializer(instance, data= request.data, partial= partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)