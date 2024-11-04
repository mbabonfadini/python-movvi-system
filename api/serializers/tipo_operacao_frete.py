from rest_framework import serializers
from ..models import TipoOperacaoFrete
from datetime import datetime



class TipoOperacaoFreteSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    descricao: str =  serializers.CharField(max_length=50)
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)



    def validate_descricao(self, value):
        if TipoOperacaoFrete.objects.filter(descricao=value).exists():
            raise serializers.ValidationError(f'O tipo de operação de frete {value} já existe.')

        return value
    

    
    def create(self, validated_data):
        tipo_operacao_frete: TipoOperacaoFrete = TipoOperacaoFrete(**validated_data)
        tipo_operacao_frete.save()

        return tipo_operacao_frete



    def update(self, instance, validated_data):
        for attrs, value in validated_data.items():
            setattr(instance, attrs, value)
        
        instance.save()
        return instance