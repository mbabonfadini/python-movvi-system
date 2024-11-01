from django.db import models

class Setor(models.Model):
    fn_setor_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, db_column='fs_setor_nome')

    class Meta:
        db_table = 't_setores'
        managed = False
    
    def __str__(self) -> str:
        return self.descricao
