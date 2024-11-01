# api/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ..serializers import LoginSerializer
from ..middleware import  TokenMiddleware

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    token_middleware = TokenMiddleware(None)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.validated_data['usuario']
        
        # Gera o token
        token_data = self.token_middleware.create_token(usuario)

        return Response(token_data, status=status.HTTP_200_OK)