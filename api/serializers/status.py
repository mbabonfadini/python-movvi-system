from rest_framework import serializers
from ..models import Status
from datetime import datetime

class StatusSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only = True)
    descricao: str = serializers.CharField(max_length=50)
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def validate_status(self, value):
        if Status.objects.filter(descricao=value).exists():
            raise serializers.ValidationError(f'Status {value} já existe! Por favor inserir valor unico!')

        return value
    
    def create(self, validated_data):
        status: Status = Status(**validated_data)
        status.save()

        return status

    def update(self, instance,validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        
        return instance