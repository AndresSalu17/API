from django.db import models

# Create your models here.

class ProjetosAndres(models.Model):
    descricao = models.CharField(max_length=100)
    stack = models.CharField(max_length=100)
    versao = models.IntegerField()
    producao = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'projeto_andres'


class ParticipantesProjeto(models.Model):
    TIPO_AREA = (
        (1, 'Frontend'),
        (2, 'Backend'),
        (3, 'Fullstack'),
        (4, 'Mobile'),
        (5, 'DevOps'),
        (6, 'Gestão de Projetos'),
        (7, 'Analise de Dados'),
        (8, 'UI/UX'),
        (9, 'Testes'),
        (10, 'Outros'),
    )
    id_projeto_andres = models.ForeignKey(ProjetosAndres, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=150, null=True, blank=True)
    area = models.IntegerField(choices=TIPO_AREA)
    contrato = models.IntegerField
    
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'projeto_participante'
        
class ContratoParticipantes(models.Model):
    id_projeto_andres = models.ForeignKey(ProjetosAndres, on_delete=models.CASCADE)
    duracao = models.IntegerField()
    valor_contrato = models.IntegerField()
    SITUACAO_CONT = (
        (1, 'Ativo'),
        (2, 'Inativo'),
    )
    situacao = models.IntegerField(choices=SITUACAO_CONT)
    resumo = models.CharField(max_length=150)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'contrato_participantes'