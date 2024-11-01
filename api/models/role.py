from django.db import models

class Role(models.Model):
    fn_role_id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=150, db_column='fs_role_nome')

    class Meta:
        db_table = 't_roles'
        managed = False

    def __str__(self):
        return self.descricao