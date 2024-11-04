from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from ..serializers import StatusSerializer
from ..models import Status
from ..utils import AuthenticatedView

class StatusListView(AuthenticatedView, generics.ListAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        return get_list_or_404(Status)

class StatusDetailView(AuthenticatedView, generics.RetrieveAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_object(self):
        status_id: int = self.kwargs.get('pk')

        return get_object_or_404(Status, pk=status_id)

class StatusCreateView(AuthenticatedView, generics.CreateAPIView):
    serializer_class =  StatusSerializer

class StatusUpdateView(AuthenticatedView, generics.UpdateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

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