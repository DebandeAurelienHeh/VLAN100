from rest_framework import serializers
from .models import Etudiant, Professeur, SalleGlobale, CoursGlobal, Absence, NoteGlobale
"""
Pour les serializers je me suis dit que récuperer toutes les informations était la chose la plus juste à faire
"""

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'

class SalleGlobaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalleGlobale
        fields = '__all__'

class CoursGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursGlobal
        fields = '__all__'

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'

class NoteGlobaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteGlobale
        fields = '__all__'

