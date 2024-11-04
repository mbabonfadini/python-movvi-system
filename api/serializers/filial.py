from rest_framework import serializers
from ..models import Filial
from datetime import datetime

class FilialSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    sigla: str = serializers.CharField(max_length=3)
    nome: str = serializers.CharField(max_length=150)
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        filial: Filial = Filial(**validated_data)
        filial.save()
        return filial

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    
    def validate_sigla(self, value):
        if Filial.objects.filter(sigla=value).exists():
            raise ValidationError("A sigla deve ser única.")
        return value