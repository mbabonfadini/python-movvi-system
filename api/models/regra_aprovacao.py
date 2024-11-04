from django.db import models
from api.models import SolicitacaoTipo, Filial, Cargo

class RegraAprovacao(models.Model):
    id: str = models.AutoField(primary_key=True, db_column='fn_regra_aprovacao_id')
    solicitacao_tipo: int = models.ForeignKey(SolicitacaoTipo, on_delete=models.RESTRICT, db_column='fn_solicitacao_tipo_id')
    filial: int = models.ForeignKey(Filial, on_delete=models.RESTRICT, db_column='fn_filial_id')
    parametro_1: str = models.CharField(max_length=150, db_column='fs_parametro_1')
    parametro_2: str = models.CharField(max_length=150, db_column='fs_parametro_2')
    parametro_3: str = models.CharField(max_length=150, db_column='fs_parametro_3')
    parametro_4: str = models.CharField(max_length=150, db_column='fs_parametro_4')
    parametro_5: str = models.CharField(max_length=150, db_column='fs_parametro_5')
    nivel_aprovacao: int = models.IntegerField(db_column='fn_aprovacao_nivel')
    cargo: int = models.ForeignKey(Cargo, on_delete=models.RESTRICT, db_column='fn_cargo_id')

    class Meta:
        db_table = 't_regras_aprovacao'
        managed = False

    def __str__(self) -> str:
        return f"Regra {self.nivel_aprovacao} - {self.solicitacao_tipo}"
