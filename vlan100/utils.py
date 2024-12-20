from ipaddress import ip_network, ip_address

VLAN_MAPPING = {
    "10.10.10.0/24": "Administration",
    "10.10.20.0/24": "Enseignants",
    "10.10.30.0/24": "Etudiants",
    "10.10.40.0/24": "Services_Generaux",
    "10.10.100.0/24": "Commun",
}

def get_vlan_from_ip(ip_address):
    """
    Associe une adresse IP à un VLAN en vérifiant les sous-réseaux.
    """
    for subnet, vlan_name in VLAN_MAPPING.items():
        if ip_address in ip_network(subnet):
            return vlan_name
    return None
