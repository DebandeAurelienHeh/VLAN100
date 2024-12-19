from rest_framework import serializers
from .models import *

# Serializer pour le modèle Etudiant
class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ['id_etudiant', 'email', 'mdp', 'nom', 'prenom', 'departement', 'statut']
        extra_kwargs = {'mdp': {'write_only': True}}

# Serializer pour le modèle Professeur
class ProfesseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professeur
        fields = '__all__'

# Serializer pour les autres modèles
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

class IncidentsGlobauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncidentsGlobaux
        fields = '__all__'

class InscriptionGlobaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscriptionGlobale
        fields = '__all__'

class PlanningGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanningGlobal
        fields = '__all__'
