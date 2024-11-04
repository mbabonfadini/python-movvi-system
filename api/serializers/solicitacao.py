from rest_framework import serializers
from ..models import Solicitacao, Usuario, SolicitacaoTipo, Status
from datetime import datetime



class SolicitacaoSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    usuario: int = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    tipo_solicitacao: int = serializers.PrimaryKeyRelatedField(queryset=SolicitacaoTipo.objects.all())
    status: int =  serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)



    def create(self, validated_data):
        solicitacao: Solicitacao = Solicitacao(**validated_data)
        solicitacao.save()
        return solicitacao



    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance