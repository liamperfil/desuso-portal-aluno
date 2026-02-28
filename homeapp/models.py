from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()
    senha = models.CharField(max_length=128) # Para armazenar a senha hash

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    carga_horaria = models.PositiveIntegerField()
    presenca_minima = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=75.0,
        help_text="Porcentagem mínima de presença (ex: 75.00)"
    )

    def __str__(self):
        return self.nome

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='turmas')
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name='turmas')
    nome_turma = models.CharField(max_length=50)
    data_inicio = models.DateField()
    data_termino = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    qtd_max_alunos = models.PositiveIntegerField()
    dias_da_semana = models.CharField(max_length=100, help_text="Ex: Segunda, Quarta, Sexta")

    def __str__(self):
        return f"{self.curso.nome} - {self.nome_turma}"

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Ativo') # Ativo, Trancado, Concluído

    class Meta:
        unique_together = ('aluno', 'turma') # Um aluno não pode se matricular duas vezes na mesma turma

    def __str__(self):
        return f"{self.aluno.nome} em {self.turma}"

class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='aulas')
    data = models.DateField()
    conteudo = models.TextField(blank=True)

    def __str__(self):
        return f"Aula de {self.turma} em {self.data}"

class Presenca(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, related_name='presencas')
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='presencas')
    presente = models.BooleanField(default=False)

    class Meta:
        unique_together = ('aula', 'aluno')

class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='notas')
    descricao = models.CharField(max_length=50) # Ex: Prova 1, Projeto Final
    valor = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.matricula.aluno.nome} - {self.descricao}: {self.valor}"

class Pagamento(models.Model):
    TIPOS_PAGAMENTO = [
        ('PIX', 'Pix'),
        ('BOLETO', 'Boleto'),
        ('ESPECIE', 'Espécie'),
    ]
    
    STATUS_PAGAMENTO = [
        ('PAGO', 'Pago'),
        ('PENDENTE', 'Pendente'),
        ('ATRASADO', 'Atrasado'),
    ]

    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='pagamentos')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    data_pagamento = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=10, choices=TIPOS_PAGAMENTO)
    status = models.CharField(max_length=10, choices=STATUS_PAGAMENTO, default='PENDENTE')

    def __str__(self):
        return f"Pagamento {self.matricula.aluno.nome} - {self.valor}"