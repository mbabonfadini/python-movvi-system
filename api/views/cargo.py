from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from ..models import Cargo
from ..serializers import CargoSerializer
from ..utils import AuthenticatedView

class CargoListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = CargoSerializer

    def get_queryset(self):
        return get_list_or_404(Cargo)

class CargoDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def get_object(self):
        cargo_id = self.kwargs.get('pk')

        return get_object_or_404(Cargo, pk=cargo_id)

class CargoCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class = CargoSerializer

class CargoUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

    def patch(self, request, *args, **kwargs):
        partial: bool = True
        return self.update(request, *args, partial= partial, **kwargs)

    def update(self, request, *args, **kwargs):
        partial: bool = kwargs.pop('partial', False)
        instance =  self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)