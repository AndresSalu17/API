from rest_framework import serializers

from appandres.models import ParticipantesProjeto, ProjetosAndres


class ProjetoAndresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetosAndres
        fields = '__all__'


class ParticipantesProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantesProjeto
        fields = '__all__'
