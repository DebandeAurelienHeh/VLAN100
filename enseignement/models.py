from django.db import models

# Modèle pour les étudiants
class Etudiant(models.Model):
    id_etudiant = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    mdp = models.CharField(max_length=255)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, null=True, blank=True)
    statut = models.BooleanField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Modèle pour les professeurs
class Professeur(models.Model):
    id_professeur = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, null=True, blank=True)
    statut = models.BooleanField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Professeurs_notes(models.Model):
    id_professeurs_notes = models.IntegerField(primary_key=True)
    id_professeur = models.IntegerField()
    id_note = models.IntegerField()

# Modèle pour les salles
class SalleGlobale(models.Model):
    id_salle = models.IntegerField(primary_key=True)
    numero_salle = models.IntegerField()
    statut = models.BooleanField()
    departement = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.numero_salle)

# Modèle pour les cours
class CoursGlobal(models.Model):
    id_cours = models.IntegerField(primary_key=True)
    nom_cours = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    id_professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    id_salle = models.ForeignKey(SalleGlobale, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_cours

# Modèle pour les absences
class Absence(models.Model):
    id_absence = models.IntegerField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE)
    date_absence = models.DateField()

    def __str__(self):
        return f"Absence de {self.id_etudiant} au cours {self.id_cours}"

# Modèle pour les notes
class NoteGlobale(models.Model):
    id_note = models.IntegerField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_saisie = models.DateField()

    def __str__(self):
        return f"Note de {self.id_etudiant} au cours {self.id_cours}"

# Modèle pour les incidents
class IncidentsGlobaux(models.Model):
    id_incident = models.IntegerField(primary_key=True)
    id_salle = models.ForeignKey(SalleGlobale, on_delete=models.CASCADE)
    description_incident = models.CharField(max_length=500)
    date_signalement = models.DateField()
    statut = models.BooleanField()

# Modèle pour les inscriptions
class InscriptionGlobale(models.Model):
    id_inscription_globale = models.IntegerField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE)
    statut = models.BooleanField()

# Modèle pour les plannings
class PlanningGlobal(models.Model):
    id_planning = models.IntegerField(primary_key=True)
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE)
    departement = models.CharField(max_length=100)
    horaire = models.TimeField()
