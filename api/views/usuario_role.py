from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from ..models import UsuarioRole
from ..serializers import UsuarioRoleSerializer
from ..utils import AuthenticatedView


class UsuarioRoleListDetailView(AuthenticatedView, generics.ListAPIView):
    serializer_class = UsuarioRoleSerializer
    
    def get_queryset(self):
        usuario_id = self.request.query_params.get('usuario')
        role_id = self.request.query_params.get('role')

        if not usuario_id and not role_id:
            return get_list_or_404(UsuarioRole)
        
        if usuario_id:
            return get_list_or_404(UsuarioRole, usuario= usuario_id)
        
        if role_id:
            return get_list_or_404(UsuarioRole, role=role_id)
        
        return UsuarioRole.objects.none()

        

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class UsuarioRoleDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = UsuarioRole.objects.all()
    serializer_class = UsuarioRoleSerializer

    def get_object(self):
        usuario_role_id: int = self.kwargs.get('pk')
        return get_object_or_404(UsuarioRole, pk=usuario_role_id)



class UsuarioRoleCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class = UsuarioRoleSerializer



class UsuarioRoleUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = UsuarioRole.objects.all()
    serializer_class = UsuarioRoleSerializer

    def patch(self, request, *args, **kwargs):
        partial: bool = True
        return self.update(request, *args, partial=partial, **kwargs)

    def update(self,  request, *args, **kwargs):
        partial: bool = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data , partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)