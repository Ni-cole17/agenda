from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    #auto now: sempre que o usuário inserir um registro, ele guarda a hora que foi feito
    #blan e null permitem que possa ficar em branco
    #max_length define o máximo de palavras naquele espaço
    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
