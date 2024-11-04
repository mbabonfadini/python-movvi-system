from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from ..serializers import TipoSenhaSerializer
from ..models import TipoSenha
from ..utils import AuthenticatedView

class TipoSenhaListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = TipoSenhaSerializer
    
    def get_queryset(self):
        return get_list_or_404(TipoSenha)



class TipoSenhaDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = TipoSenha.objects.all()
    serializer_class = TipoSenhaSerializer

    def get_object(self):
        tipo_senha_id: int = self.kwargs.get('pk')

        return get_object_or_404(TipoSenha, pk=tipo_senha_id)



class TipoSenhaCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class= TipoSenhaSerializer



class TipoSenhaUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = TipoSenha.objects.all()
    serializer_class = TipoSenhaSerializer

    def patch(self, request, *args, **kwargs):
        partial: bool = True
        return self.update(request, *args, partial=partial, **kwargs)
    
    def update(self, request, *args, **kwargs):
        partial: bool = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data= request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)