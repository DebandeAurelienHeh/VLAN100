from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Etudiant

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id_etudiant', 'nom', 'prenom', 'email', 'departement', 'statut')
