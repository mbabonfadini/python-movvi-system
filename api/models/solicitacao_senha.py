from django.db import models
from api.models import Solicitacao, TipoSenha, TipoOperacaoFrete

class SolicitacaoSenha(models.Model):
    fn_solicitacao_senha_id = models.AutoField(primary_key=True)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.RESTRICT, db_column='fn_solicitacao_id')
    tipo_senha = models.ForeignKey(TipoSenha, on_delete=models.RESTRICT, db_column='fn_tipo_senha_id')
    cotacao = models.CharField(max_length=20, db_column='fs_cotacao_id')
    valor_nota = models.DecimalField(max_digits=10, decimal_places=2, db_column='ff_valor_nota')
    peso_mercadoria = models.DecimalField(max_digits=10, decimal_places=2, db_column='ff_peso_mercadoria')
    peso_cubado_mercadoria = models.DecimalField(max_digits=10, decimal_places=2, db_column='ff_peso_cubado_mercadoria')
    valor_cotacao = models.DecimalField(max_digits=10, decimal_places=2, db_column='ff_valor_cotacao')
    remetente = models.CharField(max_length=18, db_column='fs_remetente_id')
    destinatario = models.CharField(max_length=18, db_column='fs_destinatario_id')
    consignatario = models.CharField(max_length=18, db_column='fs_consignatario_id')
    tipo_operacao_frete = models.ForeignKey(TipoOperacaoFrete, on_delete=models.RESTRICT, db_column='fn_tipo_operacao_frete_id')

    class Meta:
        db_table = 't_solicitacao_senhas'
        managed = False

    def __str__(self) -> str:
        return f'Senha {self.solicitacao} - Tipo: {self.tipo_senha}'