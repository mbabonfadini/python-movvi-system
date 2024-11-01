from django.db import models
from datetime import datetime

class Filial(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_filial_id')
    sigla: str = models.CharField(max_length=3, db_column='fs_filial_sigla')
    nome: str = models.CharField(max_length=150, db_column='fs_filial_nome')
    data_criacao: datetime = models.DateTimeField(auto_now_add=True, db_column='fd_data_criacao')
    data_atualizacao: datetime = models.DateTimeField(auto_now=True, db_column='fd_data_atualizacao')

    class Meta:
        db_table = 't_filiais'
        managed = False
    
    def __str__(self) -> str:
        return f'{self.sigla} - {self.nome}'