from django.db import models
from api.models import Usuario, Solicitacao, Status

class Aprovacao(models.Model):
    fn_aprovacao_id = models.AutoField(primary_key=True)
    solicitacao: Solicitacao = models.ForeignKey(Solicitacao, on_delete=models.RESTRICT, db_column='fn_solicitacao_id')
    nivel_aprovacao: int = models.IntegerField(db_column='fn_aprovacao_nivel')
    usuario: Usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, db_column='fn_usuario_id')
    status: Status = models.ForeignKey(Status, on_delete=models.RESTRICT, db_column='fn_status_id')

    class Meta:
        db_table = 't_aprovacoes'
        managed = False

    def __str__(self) -> str:
        return f"Aprovação {self.nivel_aprovacao} - {self.solicitacao}"
