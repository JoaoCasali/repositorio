from django.db import models
from usuarios.models import Cidadao

class Comentario(models.Model):
    descricao = models.TextField()
    resumo = models.CharField(max_length=50)
    topico = models.IntegerField()
    cidadao = models.ForeignKey(Cidadao, null=True, blank=True, on_delete=models.SET_NULL, related_name='comentarios')
    comentario_pai = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='respostas')