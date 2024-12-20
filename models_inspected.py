# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Absences(models.Model):
    id_absence = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey('Etudiants', models.DO_NOTHING, db_column='id_etudiant')
    id_cours = models.ForeignKey('CoursGlobal', models.DO_NOTHING, db_column='id_cours')
    date_absence = models.DateField()

    class Meta:
        managed = False
        db_table = 'absences'


class CoursGlobal(models.Model):
    id_cours = models.AutoField(primary_key=True)
    nom_cours = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    id_professeur = models.ForeignKey('Professeurs', models.DO_NOTHING, db_column='id_professeur')
    id_salle = models.ForeignKey('SallesGlobales', models.DO_NOTHING, db_column='id_salle')

    class Meta:
        managed = False
        db_table = 'cours_global'


class Etudiants(models.Model):
    id_etudiant = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    mdp = models.CharField(max_length=255)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, blank=True, null=True)
    statut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etudiants'


class IncidentsGlobaux(models.Model):
    id_incident = models.AutoField(primary_key=True)
    id_salle = models.ForeignKey('SallesGlobales', models.DO_NOTHING, db_column='id_salle')
    description_incident = models.CharField(max_length=500, blank=True, null=True)
    date_signalement = models.DateField()
    statut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incidents_globaux'


class InscriptionsGlobales(models.Model):
    id_inscription_globale = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='id_etudiant')
    id_cours = models.ForeignKey(CoursGlobal, models.DO_NOTHING, db_column='id_cours')
    statut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inscriptions_globales'


class NotesGlobales(models.Model):
    id_note = models.AutoField(primary_key=True)
    id_etudiant = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='id_etudiant')
    id_cours = models.ForeignKey(CoursGlobal, models.DO_NOTHING, db_column='id_cours')
    note = models.FloatField(blank=True, null=True)
    date_saisie = models.DateField()

    class Meta:
        managed = False
        db_table = 'notes_globales'


class PlanningsGlobaux(models.Model):
    id_planning = models.AutoField(primary_key=True)
    id_cours = models.ForeignKey(CoursGlobal, models.DO_NOTHING, db_column='id_cours')
    departement = models.CharField(max_length=100, blank=True, null=True)
    horaire = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plannings_globaux'


class Professeurs(models.Model):
    id_professeur = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    mdp = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, blank=True, null=True)
    statut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professeurs'


class ProfesseursNotes(models.Model):
    id_professeurs_notes = models.AutoField(primary_key=True)
    id_professeur = models.ForeignKey(Professeurs, models.DO_NOTHING, db_column='id_professeur')
    id_note = models.ForeignKey(NotesGlobales, models.DO_NOTHING, db_column='id_note')

    class Meta:
        managed = False
        db_table = 'professeurs_notes'


class SallesGlobales(models.Model):
    id_salle = models.AutoField(primary_key=True)
    numero_salle = models.IntegerField()
    statut = models.IntegerField(blank=True, null=True)
    departement = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salles_globales'
