from django import forms
from .models import Aluno, Cidade, Curso


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'