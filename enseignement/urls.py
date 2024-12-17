from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

chemin_route = DefaultRouter()

chemin_route.register(r'etudiants', EtudiantViewSet)
chemin_route.register(r'professeurs', ProfesseurViewSet)
chemin_route.register(r'salles', SalleGlobaleViewSet)
chemin_route.register(r'cours', CoursGlobalViewSet)
chemin_route.register(r'absences', AbsenceViewSet)
chemin_route.register(r'notes', NoteGlobaleViewSet)

urlpatterns = [
    path('api/', include(chemin_route.urls)),
]
