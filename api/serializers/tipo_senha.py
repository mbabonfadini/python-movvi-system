from rest_framework import serializers
from ..models import TipoSenha
from datetime import datetime



class TipoSenhaSerializer(serializers.Serializer):
    id: int = serializers.IntegerField(read_only=True)
    descricao: str = serializers.CharField(max_length=50)
    data_criacao: datetime = serializers.DateTimeField(read_only=True)
    data_atualizacao: datetime = serializers.DateTimeField(read_only=True)

    def validate_descricao(self, value):
        if TipoSenha.objects.filter(descricao=value).exists():
            raise serializers.ValidationError(f'O tipo de senha {value} já existe.')
        return value
    
    def create(self, validated_data):
        tipo_senha: TipoSenha = TipoSenha(**validated_data)
        tipo_senha.save()

        return tipo_senha
    
    def update(self, instance, validated_data):
        for attrs, value in validated_data.items():
            setattr(instance, attrs, value)
        
        instance.save()
        return instance