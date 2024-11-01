from django.db import models

class TipoOperacaoFrete(models.Model):
    fn_tipo_operacao_frete_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, db_column='fs_tipo_opercao_frete_descricao')

    class Meta:
        db_table = 't_tipo_operacao_frete'
        managed = False

    def __str__(self) -> str:
        return self.descricao