from django.db import models
from datetime import datetime

class Setor(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_setor_id')
    descricao: str = models.CharField(max_length=150, db_column='fs_setor_nome')
    data_criacao: datetime = models.DateTimeField(auto_now_add=True, db_column='fd_data_criacao')
    data_atualizacao: datetime = models.DateTimeField(auto_now=True, db_column='fd_data_atualizacao')
    
    class Meta:
        db_table = 't_setores'
        managed = False
    
    def __str__(self) -> str:
        return self.descricao
