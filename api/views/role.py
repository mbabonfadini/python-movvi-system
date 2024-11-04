from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from ..models import Role
from ..serializers import RoleSerializer
from ..utils import AuthenticatedView

class RoleListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = RoleSerializer

    def get_queryset(self):
        return get_list_or_404(Role)



class RoleDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_object(self):
        role_id: int = self.kwargs.get('pk')
        return get_object_or_404(Role, pk=role_id)



class RoleCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class = RoleSerializer




class RoleUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def patch(self, request ,*args, **kwargs):
        partial: bool = True
        return self.update(request, *args, partial=partial, **kwargs)

    def update(self, request, *args, **kwargs):
        partial:bool = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)