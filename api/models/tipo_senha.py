from django.db import models

class TipoSenha(models.Model):
    fn_tipo_senha_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, db_column='fs_tipo_senha_descricao')

    class Meta:
        db_table = 't_tipo_senha'
        managed = False

    def __str__(self) -> str:
        return self.descricao