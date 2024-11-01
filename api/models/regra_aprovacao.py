from django.db import models
from api.models import SolicitacaoTipo, Filial, Cargo

class RegraAprovacao(models.Model):
    fn_regra_aprovacao_id = models.AutoField(primary_key=True)
    solicitacao_tipo = models.ForeignKey(SolicitacaoTipo, on_delete=models.RESTRICT, db_column='fn_solicitacao_tipo_id')
    filial = models.ForeignKey(Filial, on_delete=models.RESTRICT, db_column='fn_filial_id')
    parametro_1 = models.CharField(max_length=150, db_column='fs_parametro_1')
    parametro_2 = models.CharField(max_length=150, db_column='fs_parametro_2')
    parametro_3 = models.CharField(max_length=150, db_column='fs_parametro_3')
    parametro_4 = models.CharField(max_length=150, db_column='fs_parametro_4')
    parametro_5 = models.CharField(max_length=150, db_column='fs_parametro_5')
    nivel_aprovacao = models.IntegerField(db_column='fn_aprovacao_nivel')
    cargo = models.ForeignKey(Cargo, on_delete=models.RESTRICT, db_column='fn_cargo_id')

    class Meta:
        db_table = 't_regras_aprovacao'
        managed = False

    def __str__(self) -> str:
        return f"Regra {self.nivel_aprovacao} - {self.solicitacao_tipo}"
