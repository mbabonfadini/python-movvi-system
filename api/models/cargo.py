from django.db import models
from api.models import Status

class Cargo(models.Model):
    fn_cargo_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, db_column='fs_cargo_descricao')
    status = models.ForeignKey(Status, on_delete=models.RESTRICT, db_column='fn_status_id')

    class Meta:
        db_table = 't_cargos'
        managed = False

    def __str__(self) -> str:
        return self.descricao
    