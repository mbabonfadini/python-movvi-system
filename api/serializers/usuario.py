from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from ..models import Usuario, Filial, Setor, Cargo, Status
from datetime import datetime

class UsuarioSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    nome: str = serializers.CharField(max_length=150)
    sobrenome: str = serializers.CharField(max_length=150)
    email: str = serializers.EmailField()
    senha: str = serializers.CharField(write_only=True)
    filial = serializers.PrimaryKeyRelatedField(queryset=Filial.objects.all())
    setor = serializers.PrimaryKeyRelatedField(queryset=Setor.objects.all())
    cargo = serializers.PrimaryKeyRelatedField(queryset=Cargo.objects.all())
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        if not attrs.get('senha'):
            raise serializers.ValidationError("A senha não pode estar em branco.")
        return attrs
    
    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data.pop('senha'))  # Corrigido aqui
        usuario = Usuario(**validated_data)
        usuario.save()
        return usuario
    
    def update(self, instance, validated_data):
        senha_nova = validated_data.pop('senha', None)

        if senha_nova:
            instance.senha = make_password(senha_nova)

        # Atualiza os demais campos
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance