from rest_framework import serializers
from ..models import SolicitacaoTipo
from datetime import datetime



class SolicitacaoTipoSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    descricao: str = serializers.CharField(max_length=150)
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def validate_descricao(self, value):
        if SolicitacaoTipo.objects.filter(descricao=value).exists():
            raise serializers.ValidationError(f"O Tipo de solicitação '{value}' já existe")
        
        return value

    

    def create(self, validated_data):
        solicitacao_tipo: SolicitacaoTipo = SolicitacaoTipo(**validated_data)
        solicitacao_tipo.save()
        return solicitacao_tipo



    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance