from django.db import models

class Filial(models.Model):
    fn_filial_id = models.AutoField(primary_key=True)
    sigla = models.CharField(max_length=3, db_column='fs_filial_sigla')
    nome = models.CharField(max_length=150, db_column='fs_filial_nome')

    class Meta:
        db_table = 't_filiais'
        managed = False
    
    def __str__(self) -> str:
        return f'{self.sigla} - {self.nome}'