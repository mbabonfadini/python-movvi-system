from rest_framework import serializers
from ..models import Role
from datetime import datetime

class RoleSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    descricao: str = serializers.CharField(max_length=150)
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)
    
    def validate_descricao(self, value): 
        if Role.objects.filter(descricao=value).exists():
            raise serializers.ValidationError(f'A role {value} já existe!')
        return value
    
    def create(self, validated_data):
        role: Role = Role(**validated_data)
        role.save()
        return role

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        
        return instance
