from django.db import models
from api.models import Filial, Status, Setor, Cargo
from datetime import datetime

class Usuario(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_usuario_id')
    nome: str = models.CharField(max_length=150, db_column='fs_usuario_nome')
    sobrenome: str = models.CharField(max_length=150, db_column='fs_usuario_sobrenome')
    email: str = models.EmailField(unique=True, db_column='fs_usuario_email')
    senha: str = models.CharField(max_length=255, db_column='fs_usuario_senha_hash')
    filial: int = models.ForeignKey(Filial, on_delete=models.RESTRICT, db_column='fn_filial_id')
    setor: int = models.ForeignKey(Setor, on_delete=models.RESTRICT, db_column='fn_setor_id')
    status: int = models.ForeignKey(Status, on_delete=models.RESTRICT, db_column='fn_status_id')
    cargo: int = models.ForeignKey(Cargo, on_delete=models.RESTRICT, db_column='fn_cargo_id')
    data_criacao: datetime = models.DateTimeField(auto_now_add=True, db_column='fd_data_criacao')
    data_atualizacao: datetime = models.DateTimeField(auto_now=True, db_column='fd_data_atualizacao')

    class Meta:
        db_table = 't_usuarios'
        managed = False
    
    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'