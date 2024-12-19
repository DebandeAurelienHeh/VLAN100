from django.contrib.auth.hashers import make_password
from django.db import models


# Modèle pour les étudiants
class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    mdp = models.CharField(max_length=255)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, null=True, blank=True)
    statut = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Hachage du mot de passe uniquement si nécessaire
        if not self.mdp.startswith('pbkdf2_'):
            self.mdp = make_password(self.mdp)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        db_table = 'etudiants'
        managed = False


# Modèle pour les professeurs
class Professeur(models.Model):
    id_professeur = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=255)
    departement = models.CharField(max_length=100, null=True, blank=True)
    statut = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

    class Meta:
        db_table = 'professeurs'
        managed = False


# Modèle pour les salles
class SalleGlobale(models.Model):
    id_salle = models.AutoField(primary_key=True)
    numero_salle = models.IntegerField()
    statut = models.BooleanField(default=True)
    departement = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Salle {self.numero_salle}"

    class Meta:
        db_table = 'salles_globales'
        managed = False


# Modèle pour les cours
class CoursGlobal(models.Model):
    id_cours = models.AutoField(primary_key=True)
    nom_cours = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    id_professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE, db_column='id_professeur')
    id_salle = models.ForeignKey(SalleGlobale, on_delete=models.CASCADE, db_column='id_salle')

    def __str__(self):
        return self.nom_cours

    class Meta:
        db_table = 'cours_global'
        managed = False


# Modèle pour les absences
class Absence(models.Model):
    id_absence = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, db_column='id_etudiant')
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE, db_column='id_cours')
    date_absence = models.DateField()

    def __str__(self):
        return f"Absence de {self.id_etudiant} au cours {self.id_cours}"

    class Meta:
        db_table = 'absences'
        managed = False


# Modèle pour les notes
class NoteGlobale(models.Model):
    id_note = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, db_column='id_etudiant')
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE, db_column='id_cours')
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_saisie = models.DateField()

    def __str__(self):
        return f"Note de {self.id_etudiant} au cours {self.id_cours}"

    class Meta:
        db_table = 'notes_globales'
        managed = False


# Modèle pour les incidents
class IncidentsGlobaux(models.Model):
    id_incident = models.AutoField(primary_key=True)
    id_salle = models.ForeignKey(SalleGlobale, on_delete=models.CASCADE, db_column='id_salle')
    description_incident = models.TextField(default="Aucune description")
    date_signalement = models.DateField()
    statut = models.BooleanField(default=True)

    class Meta:
        db_table = 'incidents_globaux'
        managed = False


# Modèle pour les inscriptions
class InscriptionGlobale(models.Model):
    id_inscription_globale = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, db_column='id_etudiant')
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE, db_column='id_cours')
    statut = models.BooleanField(default=True)

    class Meta:
        db_table = 'inscriptions_globales'
        managed = False


# Modèle pour les plannings
class PlanningGlobal(models.Model):
    id_planning = models.AutoField(primary_key=True)
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE, db_column='id_cours')
    departement = models.CharField(max_length=100)
    horaire = models.TimeField()

    class Meta:
        db_table = 'plannings'
        managed = False
