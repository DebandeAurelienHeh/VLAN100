# Create your views here.
"""
Ici seront faites nos API
"""
from rest_framework import viewsets

from .serializers import *


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

class IncdientGlobaux(viewsets.ModelViewSet):
