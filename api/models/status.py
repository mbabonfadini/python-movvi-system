from django.db import models

class Status(models.Model):
    id: int = models.AutoField(primary_key=True, db_column='fn_status_id')
    descricao: str = models.CharField(max_length=50, db_column='fs_status_descricao')

    class Meta:
        db_table = 't_status'
        managed = False
    
    def __str__(self) -> str:
        return self.descricao