from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)
    
    def __str__(self) -> str:
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveSmallIntegerField()
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    curso = models.ForeignKey('Curso', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.nome