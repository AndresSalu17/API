from rest_framework import serializers

from appandres.models import ContratoParticipantes, ParticipantesProjeto, ProjetosAndres


class ProjetoAndresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjetosAndres
        fields = '__all__'


class ParticipantesProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantesProjeto
        fields = '__all__'
        
class ContratoParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContratoParticipantes
        fields = '__all__'
