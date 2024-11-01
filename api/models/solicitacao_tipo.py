from django.db import models

class SolicitacaoTipo(models.Model):
    fn_solicitacao_tipo_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, db_column='fs_solicitacao_tipo_descricao')

    class Meta:
        db_table = 't_solicitacao_tipo'
        managed = False

    def __str__(self) -> str:
        return self.descricao
    