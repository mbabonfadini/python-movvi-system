from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from ..models import TipoOperacaoFrete
from ..serializers import TipoOperacaoFreteSerializer
from ..utils import AuthenticatedView



class TipoOperacaoFreteListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = TipoOperacaoFreteSerializer

    def get_queryset(self):
        return get_list_or_404(TipoOperacaoFrete)



class TipoOperacaoFreteDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = TipoOperacaoFrete.objects.all()
    serializer_class = TipoOperacaoFreteSerializer

    def get_object(self):
        tipo_operacao_frete_id: int = self.kwargs.get('pk')

        return get_object_or_404(TipoOperacaoFrete, pk= tipo_operacao_frete_id)



class TipoOperacaoFreteCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class = TipoOperacaoFreteSerializer



class TipoOperacaoFreteUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = TipoOperacaoFrete
    serializer_class = TipoOperacaoFreteSerializer



    def patch(self, request, *args, **kwargs):
        partial: bool = True
        return self.update(request, *args, partial=partial, **kwargs)



    def update(self, request, *args, **kwargs):
        partial: bool = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)