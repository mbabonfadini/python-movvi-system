from django.db import models
from api.models import SolicitacaoSenha, Status
import hashlib

class SolicitacaoSenhaChave(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_solicitacao_senha_chave_id')
    solicitacao_senha: int  = models.ForeignKey(SolicitacaoSenha, on_delete=models.RESTRICT, db_column='fn_solicitacao_senha_id')
    chave: str = models.CharField(max_length=10, db_column='fs_solicitacao_senha_chave', unique=True)
    status: int = models.ForeignKey(Status, on_delete=models.CASCADE, db_column='fn_status_id')

    class Meta:
        db_table = 't_solicitacao_senha_chave'
        managed = False

    def generate_chave(self, sigla_filial: str, id_solicitacao: int, remetente: str) -> str:
        import hashlib
        raw_key = f"{sigla_filial}{id_solicitacao}{remetente}"
        hashed_key = hashlib.sha256(raw_key.encode()).hexdigest()
        return hashed_key[:10]

    def save(self, *args, **kwargs):
        if not self.chave:
            sigla_filial = kwargs.pop('sigla_filial', None)
            id_solicitacao = self.solicitacao_senha.id
            remetente = kwargs.pop('remetente', None)

            if sigla_filial and remetente:
                self.chave = self.generate_chave(sigla_filial, id_solicitacao, remetente)

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.chave