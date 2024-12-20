from ldap3 import Server, Connection, ALL
from django.contrib.auth.models import User, Group
from django.conf import settings
from ipaddress import ip_network, ip_address

# Définition des plages IP pour chaque VLAN
VLAN_RANGES = {
    "administration": ip_network("10.10.10.0/24"),
    "enseignants": ip_network("10.10.20.0/24"),
    "etudiants": ip_network("10.10.30.0/24"),
    "services_generaux": ip_network("10.10.40.0/24"),
    "commun": ip_network("10.10.100.0/24"),
}

def get_vlan_from_ip(ip):
    for vlan, network in VLAN_RANGES.items():
        if ip_address(ip) in network:
            return vlan
    return None

class LDAPBackend:
    """
    Backend d'authentification LDAP avec vérification VLAN.
    """

    def authenticate(self, request, username=None, password=None):
        ip_user = request.META.get('REMOTE_ADDR')  # Récupérer l'adresse IP de l'utilisateur
        vlan = get_vlan_from_ip(ip_user)

        if vlan is None:
            return None  # Accès refusé si l'IP ne correspond à aucun VLAN

        conn = self._get_connection(username, password)
        if conn and conn.bind():
            return self._get_or_create_user(username, vlan)
        return None

    def _get_connection(self, username, password):
        server = Server(settings.LDAP_SERVER, get_info=ALL)
        return Connection(server, f"CN={username},{settings.LDAP_BASE_DN}", password)

    def _get_or_create_user(self, username, vlan):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.set_unusable_password()
            user.save()

        # Associer l'utilisateur à un groupe correspondant au VLAN
        group, created = Group.objects.get_or_create(name=vlan)
        user.groups.add(group)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
