from django.contrib import admin
from .models import Professor, Aluno, Curso, Turma, Matricula, Aula, Presenca, Nota, Pagamento

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'cpf')

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'cpf')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria', 'presenca_minima')

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome_turma', 'curso', 'professor', 'data_inicio', 'qtd_max_alunos')
    list_filter = ('curso', 'professor', 'dias_da_semana')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'turma', 'data_matricula', 'status')
    list_filter = ('status', 'turma')
    search_fields = ('aluno__nome',)

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('turma', 'data', 'conteudo')
    list_filter = ('turma', 'data')

@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    list_display = ('aula', 'aluno', 'presente')
    list_filter = ('presente', 'aula__turma')

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('get_aluno', 'get_turma', 'descricao', 'valor')
    list_filter = ('matricula__turma', 'descricao')

    def get_aluno(self, obj):
        return obj.matricula.aluno.nome
    get_aluno.short_description = 'Aluno'

    def get_turma(self, obj):
        return obj.matricula.turma.nome_turma
    get_turma.short_description = 'Turma'

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('get_aluno', 'valor', 'data_vencimento', 'tipo', 'status')
    list_filter = ('status', 'tipo', 'data_vencimento')
    
    def get_aluno(self, obj):
        return obj.matricula.aluno.nome
    get_aluno.short_description = 'Aluno'