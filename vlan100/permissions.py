from rest_framework.permissions import BasePermission
from vlan100.utils import get_vlan_from_ip  # Import de la fonction utils pour détecter les VLANs

class IsFromAuthorizedVLANOrGroup(BasePermission):
    """
    Permission basée sur les VLANs et les groupes AD.
    """

    def has_permission(self, request, view):
        client_ip = request.META.get('REMOTE_ADDR')  # Adresse IP de l'utilisateur
        vlan = get_vlan_from_ip(client_ip)  # Détecte le VLAN associé à l'IP

        if vlan is None:
            return False
        if view.basename == "etudiant" and vlan in ["Administration", "Etudiants"]:
            return True
        if view.basename == "professeur" and vlan in ["Administration", "Enseignants"]:
            return True
        if view.basename == "salles" and vlan in ["Administration", "Services_Generaux"]:
            return True
        if view.basename == "cours" and vlan in ["Administration", "Enseignants"]:
            return True
        if view.basename == "planning" and vlan in ["Administration", "Enseignants", "Etudiants"]:
            return True

        return False
