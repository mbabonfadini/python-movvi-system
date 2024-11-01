from django.db import models
from api.models import Usuario, SolicitacaoTipo, Status

class Solicitacao(models.Model):
    fn_solicitacao_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, db_column='fn_usuario_id')
    tipo_solicitacao = models.ForeignKey(SolicitacaoTipo, on_delete=models.RESTRICT, db_column='fn_solicitacao_tipo_id')
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, db_column='fn_status_id')

    class Meta:
        db_table = 't_solicitacao'
        managed = False

    def __str__(self) -> str:
        return f'{self.usuario} - {self.tipo_solicitacao} - {self.status}'
    