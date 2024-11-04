from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from ..models import Usuario
from ..serializers import UsuarioSerializer
from ..utils import AuthenticatedView, CustomPagination
# Create your views here.

class UsuarioListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = UsuarioSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return get_list_or_404(Usuario) 



class UsuarioDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_object(self):
        usuario_id = self.kwargs.get('pk')
        return get_object_or_404(Usuario, pk=usuario_id)



class UsuarioCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class = UsuarioSerializer



class UsuarioUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset= Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def patch(self, request, *args, **kwargs):
        partial = True  # Permite a atualização parcial
        return self.update(request, *args, partial=partial, **kwargs)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)