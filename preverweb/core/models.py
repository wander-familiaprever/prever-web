from django.db import models

class Usuarios(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length = 30)
    nick = models.CharField(max_length = 10)
    
    class Meta:
        managed = False
        db_table = 'usuarios'

