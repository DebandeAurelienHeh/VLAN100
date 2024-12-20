from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView

from vlan100.auth_backends import get_vlan_from_ip
from .serializers import *
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def ldap_login_view(request):
    if request.method == "POST":
        return _handle_post_request(request)
    return JsonResponse({"status": "error", "message": "Invalid request method"})

def _handle_post_request(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user:
        return _process_authenticated_user(request, user)
    return JsonResponse({"status": "error", "message": "Invalid credentials"})

def _process_authenticated_user(request, user):
    ip_user = request.META.get('REMOTE_ADDR')
    vlan = get_vlan_from_ip(ip_user)
    if vlan:
        login(request, user)
        return JsonResponse({"status": "success", "message": f"Welcome {user.username}", "vlan": vlan})
    return JsonResponse({"status": "error", "message": "Unauthorized VLAN"})

class RestrictedAPIView(APIView):
    def get(self, request):
        client_ip = request.META.get('REMOTE_ADDR')
        vlan = get_vlan_from_ip(client_ip)

        if vlan == "Etudiants":
            return Response({"message": "Accès aux données des étudiants"})
        elif vlan == "Enseignants":
            return Response({"message": "Accès aux données des enseignants"})
        return Response({"error": "Accès interdit"}, status=403)

# Exemple pour Etudiants
class EtudiantViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['departement', 'statut']
    search_fields = ['nom', 'prenom', 'email']

    def get_queryset(self):
        user_groups = self.request.user.groups.values_list('name', flat=True)
        if "etudiants" in user_groups:
            return self.queryset.filter(departement="etudiants")
        return self.queryset.none()

# Vues similaires pour les autres modèles
class ProfesseurViewSet(viewsets.ModelViewSet):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nom', 'prenom', 'email']

class SalleGlobaleViewSet(viewsets.ModelViewSet):
    queryset = SalleGlobale.objects.all()
    serializer_class = SalleGlobaleSerializer

class CoursGlobalViewSet(viewsets.ModelViewSet):
    queryset = CoursGlobal.objects.all()
    serializer_class = CoursGlobalSerializer

class AbsenceViewSet(viewsets.ModelViewSet):
    queryset = Absence.objects.all()
    serializer_class = AbsenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_etudiant', 'id_cours', 'date_absence']

class NoteGlobaleViewSet(viewsets.ModelViewSet):
    queryset = NoteGlobale.objects.all()
    serializer_class = NoteGlobaleSerializer

class IncidentsGlobauxViewSet(viewsets.ModelViewSet):
    queryset = IncidentsGlobaux.objects.all()
    serializer_class = IncidentsGlobauxSerializer

class InscriptionGlobaleViewSet(viewsets.ModelViewSet):
    queryset = InscriptionGlobale.objects.all()
    serializer_class = InscriptionGlobaleSerializer

class PlanningGlobalViewSet(viewsets.ModelViewSet):
    queryset = PlanningGlobal.objects.all()
    serializer_class = PlanningGlobalSerializer
