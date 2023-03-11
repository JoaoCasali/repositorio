from django.db import models
from django.contrib.auth.models import AbstractUser

class Cidadao(AbstractUser):
    id = models.AutoField(primary_key=True, null=False)
    cpf_cnpj = models.CharField(max_length=14)