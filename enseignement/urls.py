from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'etudiants', EtudiantViewSet, basename='etudiant')
router.register(r'professeurs', ProfesseurViewSet, basename='professeur')
router.register(r'salles', SalleGlobaleViewSet, basename='salleglobale')
router.register(r'cours', CoursGlobalViewSet, basename='coursglobal')
router.register(r'absences', AbsenceViewSet, basename='absence')
router.register(r'notes', NoteGlobaleViewSet, basename='noteglobal')
router.register(r'incidents', IncidentsGlobauxViewSet, basename='incidentglobaux')
router.register(r'inscriptions', InscriptionGlobaleViewSet, basename='inscriptionglobale')
router.register(r'plannings', PlanningGlobalViewSet, basename='planningglobal')

urlpatterns = [
    path('api/', include(router.urls)),
]
