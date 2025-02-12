from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from appandres.models import ContratoParticipantes, ParticipantesProjeto, ProjetosAndres
from appandres.serializers import ContratoParticipantesSerializer, ParticipantesProjetoSerializer, ProjetoAndresSerializer

# Create your views here.

class ProjetosAndresViewset(viewsets.ModelViewSet):
    queryset = ProjetosAndres.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjetoAndresSerializer
    ordering_fields = ('id',)
    filterset_fields = ('id', 'stack', 'producao')
    search_fields = ('stack', 'producao')


class ParticipantesProjetoViewSet(viewsets.ModelViewSet):
    queryset = ParticipantesProjeto.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ParticipantesProjetoSerializer
    ordering_field = ('id',)
    filterset_fields = ('id', 'nome', 'area')
    
class ContratoParticipantesViewSet(viewsets.ModelViewSet):
    queryset = ContratoParticipantes.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContratoParticipantesSerializer
    ordering_field = ('id',)
    
    