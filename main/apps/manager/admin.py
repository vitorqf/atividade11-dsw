from django.contrib import admin

from .models import Cidade, Aluno, Curso

# Register your models here.
admin.site.register(Cidade)
admin.site.register(Aluno)
admin.site.register(Curso)