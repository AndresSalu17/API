from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from appandres.models import ProjetosAndres
from appandres.serializers import ProjetoAndresSerializer

# Create your views here.

class ProjetosAndresViewset(viewsets.ModelViewSet):
    queryset = ProjetosAndres.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProjetoAndresSerializer
    ordering_fields = ('id',)
    filterset_fields = ('id', 'stack', 'producao')
    search_fields = ('stack', 'producao')

