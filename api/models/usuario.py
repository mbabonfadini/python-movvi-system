from django.db import models
from api.models import Filial, Status, Setor, Cargo

class Usuario(models.Model):
    fn_usuario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, db_column='fs_usuario_nome')
    sobrenome = models.CharField(max_length=150, db_column='fs_usuario_sobrenome')
    email = models.EmailField(unique=True, db_column='fs_usuario_email')
    senha_hash = models.CharField(max_length=255, db_column='fs_usuario_senha_hash')
    filial = models.ForeignKey(Filial, on_delete=models.RESTRICT, db_column='fn_filial_id')
    setor = models.ForeignKey(Setor, on_delete=models.RESTRICT, db_column='fn_setor_id')
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, db_column='fn_status_id')
    cargo = models.ForeignKey(Cargo, on_delete=models.RESTRICT, db_column='fn_cargo_id')

    class Meta:
        db_table = 't_usuarios'
        managed = False
    
    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'