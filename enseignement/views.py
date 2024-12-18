# Create your views here.
"""
Ici seront faites nos API
"""
from rest_framework import viewsets
from .models import (
    Etudiant, Professeur, SalleGlobale, CoursGlobal, Absence, NoteGlobale,
    IncidentsGlobaux, InscriptionGlobale, PlanningGlobal
)
from .serializers import (
    EtudiantSerializer, ProfesseurSerializer, SalleGlobaleSerializer,
    CoursGlobalSerializer, AbsenceSerializer, NoteGlobaleSerializer,
    IncidentsGlobauxSerializer, InscriptionGlobaleSerializer, PlanningGlobalSerializer
)

class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class ProfesseurViewSet(viewsets.ModelViewSet):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer

class SalleGlobaleViewSet(viewsets.ModelViewSet):
    queryset = SalleGlobale.objects.all()
    serializer_class = SalleGlobaleSerializer

class CoursGlobalViewSet(viewsets.ModelViewSet):
    queryset = CoursGlobal.objects.all()
    serializer_class = CoursGlobalSerializer

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer

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
