from django.db import models

# Modèle pour les étudiants
class Etudiant(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    mdp = models.CharField(max_length=255)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, null=True, blank=True)
    statut = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Modèle pour les professeurs
class Professeur(models.Model):
    id_professeur = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=255)
    departement = models.CharField(max_length=100, null=True, blank=True)
    statut = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

# Modèle pour les salles
class SalleGlobale(models.Model):
    id_salle = models.AutoField(primary_key=True)
    numero_salle = models.CharField(max_length=50)
    statut = models.CharField(max_length=50, null=True, blank=True)
    departement = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.numero_salle

# Modèle pour les cours
class CoursGlobal(models.Model):
    id_cours = models.AutoField(primary_key=True)
    nom_cours = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    id_professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    id_salle = models.ForeignKey(SalleGlobale, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_cours

# Modèle pour les absences
class Absence(models.Model):
    id_absence = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE)
    date_absence = models.DateField()

    def __str__(self):
        return f"Absence de {self.id_etudiant} au cours {self.id_cours}"

# Modèle pour les notes
class NoteGlobale(models.Model):
    id_note = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    id_cours = models.ForeignKey(CoursGlobal, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    date_saisie = models.DateField()

    def __str__(self):
        return f"Note de {self.id_etudiant} au cours {self.id_cours}"
class IncidentsGlobaux(models.Model):
    pass