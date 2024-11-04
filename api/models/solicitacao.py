from django.db import models
from api.models import Usuario, SolicitacaoTipo, Status
from datetime import datetime

class Solicitacao(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_solicitacao_id')
    usuario: str = models.ForeignKey(Usuario, on_delete=models.RESTRICT, db_column='fn_usuario_id')
    tipo_solicitacao: int = models.ForeignKey(SolicitacaoTipo, on_delete=models.RESTRICT, db_column='fn_solicitacao_tipo_id')
    status: int = models.ForeignKey(Status, on_delete=models.RESTRICT, db_column='fn_status_id')
    data_criacao: datetime = models.DateTimeField(auto_now_add=True, db_column='fd_data_criacao')
    data_atualizacao: datetime = models.DateTimeField(auto_now=True, db_column='fd_data_atualizacao')

    class Meta:
        db_table = 't_solicitacao'
        managed = False

    def __str__(self) -> str:
        return f'{self.usuario} - {self.tipo_solicitacao} - {self.status}'
    