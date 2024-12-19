from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Exemple pour Etudiants
class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['departement', 'statut']  # Filtrage par département et statut
    search_fields = ['nom', 'prenom', 'email']  # Recherche par nom, prénom ou email

# Vues similaires pour les autres modèles
class ProfesseurViewSet(viewsets.ModelViewSet):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nom', 'prenom', 'email']

class SalleGlobaleViewSet(viewsets.ModelViewSet):
    queryset = SalleGlobale.objects.all()
    serializer_class = SalleGlobaleSerializer

class CoursGlobalViewSet(viewsets.ModelViewSet):
    queryset = CoursGlobal.objects.all()
    serializer_class = CoursGlobalSerializer

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_etudiant', 'id_cours', 'date_absence']

class NoteGlobaleViewSet(viewsets.ModelViewSet):
    queryset = NoteGlobale.objects.all()
    serializer_class = NoteGlobaleSerializer

class IncidentsGlobauxViewSet(viewsets.ModelViewSet):
    queryset = IncidentsGlobaux.objects.all()
    serializer_class = IncidentsGlobauxSerializer

class InscriptionGlobaleViewSet(viewsets.ModelViewSet):
    queryset = InscriptionGlobale.objects.all()
    serializer_class = InscriptionGlobaleSerializer

class PlanningGlobalViewSet(viewsets.ModelViewSet):
    queryset = PlanningGlobal.objects.all()
    serializer_class = PlanningGlobalSerializer
