from rest_framework import serializers
from ..models import Cargo, Status
from datetime import datetime

class CargoSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    descricao: str = serializers.CharField(max_length=150)
    status: int = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def validate_cargo(self, value):
        if Cargo.objects.filter(descricao=value).exists():
            raise serializers.ValidationError(f'Cargo {value} já existe! Por favor inserir valor unico!')
        
        return value
    
    def create(self, validated_data):
        cargo: Cargo = Cargo(**validated_data)
        cargo.save()
        return cargo

    def update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
