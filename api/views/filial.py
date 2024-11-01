from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from ..utils import AuthenticatedView
from ..models import Filial
from ..serializers import FilialSerializer

class FilialListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = FilialSerializer

    def get_queryset(self):
        return get_list_or_404(Filial)

class FilialDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer

    def get_object(self):
        filial_id = self.kwargs.get('pk')
        return get_object_or_404(Filial, pk=filial_id)

class FilialCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class = FilialSerializer

class FilialUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer

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

