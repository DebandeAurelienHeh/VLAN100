from rest_framework import serializers
from .models import *

# /!\ je dois encore verifier avec Adam

# Serializer pour le modèle Etudiant
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'

# Serializer pour le modèle Professeur
class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'

# Serializer pour le modèle SalleGlobale
class SalleGlobaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalleGlobale
        fields = '__all__'

# Serializer pour le modèle CoursGlobal
class CoursGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursGlobal
        fields = '__all__'

# Serializer pour le modèle Absence
class AbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absence
        fields = '__all__'

# Serializer pour le modèle NoteGlobale
class NoteGlobaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteGlobale
        fields = '__all__'

# Serializer pour le modèle IncidentsGlobaux
class IncidentsGlobauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentsGlobaux
        fields = '__all__'

# Serializer pour le modèle InscriptionGlobale
class InscriptionGlobaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionGlobale
        fields = '__all__'

# Serializer pour le modèle PlanningGlobal
class PlanningGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanningGlobal
        fields = '__all__'
