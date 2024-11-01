from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class AuthenticatedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]