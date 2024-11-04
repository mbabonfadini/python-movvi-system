from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from ..models import Usuario

class LoginSerializer(serializers.Serializer):
    email: str = serializers.EmailField()
    senha: str = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email: str = attrs.get('email')
        senha: str = attrs.get('senha')

        try:
            usuario: Usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Credenciais inválidas.")
        
        if usuario.status.id != 1:
            raise serializers.ValidationError("Credenciais inválidas.")

        if not check_password(senha, usuario.senha):
            raise serializers.ValidationError("Credenciais inválidas.")

        attrs['usuario'] = usuario
        return attrs