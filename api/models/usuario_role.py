from django.db import models
from api.models import Usuario, Role, Status

class UsuarioRole(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_usuario_role_id')
    usuario: int = models.ForeignKey(Usuario, on_delete=models.RESTRICT, db_column='fn_usuario_id')
    role: int = models.ForeignKey('Role', on_delete=models.RESTRICT, db_column='fn_role_id')
    status: int = models.ForeignKey(Status, on_delete=models.RESTRICT, db_column='fn_status_id')

    class Meta:
        db_table = 't_usuario_roles'
        managed = False

    def __str__(self) -> str:
        return f'{self.usuario} - {self.role} - {self.status}'
