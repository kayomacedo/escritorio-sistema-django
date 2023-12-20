from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    # Adicione quaisquer outros campos relevantes para a pessoa

    def __str__(self):
        return self.nome

class Documento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    resumo = models.TextField(max_length=255)
    pessoas_envolvidas = models.ManyToManyField(Pessoa)  # Relacionamento ManyToManyField
    endereco = models.CharField(max_length=255)
    data_documento = models.DateField()
    tamanho_area = models.CharField(max_length=255)
    local_armazenamento = models.CharField(max_length=255)
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo