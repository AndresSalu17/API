from django.contrib import admin

from appandres.models import ParticipantesProjeto, ProjetosAndres

# Register your models here.

class ProjetoAndresAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'stack', 'versao', 'producao', 'criado_em', 'atualizado_em')
    list_filter = ('id',)
    search_fields = ('id', 'stack')
admin.site.register(ProjetosAndres, ProjetoAndresAdmin)

class ParticipantesProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_projeto_andres', 'nome', 'email', 'area')
    list_filter = ('id', 'area')
    search_fields = ('id', 'nome')
admin.site.register(ParticipantesProjeto, ParticipantesProjetoAdmin)    