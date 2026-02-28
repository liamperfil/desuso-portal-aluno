from django import forms
from .models import Professor, Aluno, Curso, Turma, Matricula

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'cpf', 'email', 'telefone']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'email', 'telefone', 'data_nascimento']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao', 'carga_horaria', 'presenca_minima']

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['curso', 'professor', 'nome_turma', 'data_inicio', 'data_termino', 'horario_inicio', 'horario_fim', 'qtd_max_alunos', 'dias_da_semana']

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['aluno', 'turma', 'status']