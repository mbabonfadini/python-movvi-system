from django.db import models
from datetime import datetime



class TipoOperacaoFrete(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_tipo_operacao_frete_id')
    descricao: str = models.CharField(max_length=50, db_column='fs_tipo_opercao_frete_descricao')
    data_criacao: datetime = models.DateTimeField(auto_now_add=True, db_column='fd_data_criacao')
    data_atualizacao: datetime = models.DateTimeField(auto_now=True, db_column='fd_data_atualizacao')



    class Meta:
        db_table = 't_tipo_operacao_frete'
        managed = False



    def __str__(self) -> str:
        return self.descricao