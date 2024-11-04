from rest_framework import serializers
from ..models import Setor
from datetime import datetime

class SetorSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    descricao: str = serializers.CharField(max_length=150)
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def validate_setor(self, value):
        if Setor.objects.filter(descricao=value).exists():
            raise ValidationError("Este setor já existe!")
        return value

    def create(self, validated_data):
        setor: Setor = Setor(**validated_data)
        setor.save()
        
        return setor

    def update(self, instance, validated_data):
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        
        return instance
