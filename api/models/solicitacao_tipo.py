from django.db import models
from datetime import datetime



class SolicitacaoTipo(models.Model):
    id: int = models.AutoField(primary_key=True,db_column='fn_solicitacao_tipo_id')
    descricao: str = models.CharField(max_length=150, db_column='fs_solicitacao_tipo_descricao')
    data_criacao: datetime = models.DateTimeField(auto_now_add=True, db_column='fd_data_criacao')
    data_atualizacao: datetime = models.DateTimeField(auto_now=True, db_column='fd_data_atualizacao')

    class Meta:
        db_table = 't_solicitacao_tipo'
        managed = False

    def __str__(self) -> str:
        return self.descricao
    