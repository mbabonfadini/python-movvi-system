from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from ..serializers import SetorSerializer
from ..models import Setor

class SetorListView(generics.ListAPIView):
    serializer_class = SetorSerializer

    def get_queryset(self):
        return get_list_or_404(Setor)

class SetorDetailView(generics.RetrieveAPIView):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

    def get_object(self):
        setor_id = self.kwargs.get('pk')
        return get_object_or_404(Setor, pk=setor_id)
    
class SetorCreateView(generics.CreateAPIView):
    serializer_class = SetorSerializer

class SetorUpdateView(generics.UpdateAPIView):
    queryset = Setor.objects.all()
    serializer_class =SetorSerializer

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