from rest_framework import serializers
from ..models import UsuarioRole, Usuario, Role, Status
from datetime import datetime



class UsuarioRoleSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    usuario: int = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    role: int = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    status: int = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def validate(self, attrs):
        usuario = attrs.get('usuario')
        role = attrs.get('role')
        novo_status = attrs.get('status')

        usuario_role = UsuarioRole.objects.filter(usuario=usuario, role=role).first()
        
        if usuario_role:
            status_atual = usuario_role.status

            if status_atual == novo_status:
                raise serializers.ValidationError("Usuario Já possui está liberação com o mesmo status.")

        return attrs

    def create(self, validated_data):
        usuario_role = UsuarioRole(**validated_data)
        usuario_role.save()
        return usuario_role

    def update(self, instance, validated_data):
        for attrs, value in validated_data.items():
            setattr(instance, attrs, value)
        
        instance.save()
        return instance