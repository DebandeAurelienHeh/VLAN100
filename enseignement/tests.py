import os
import django
from django.test import TestCase
from .models import Etudiant

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vlan100.settings')  # Remplacez 'vlan100' par le nom correct du projet si nécessaire.
django.setup()

class EtudiantModelTest(TestCase):
    def setUp(self):
        self.etudiant = Etudiant.objects.create(
            email="test@example.com",
            mdp="password123",
            nom="Test",
            prenom="User",
            departement="Informatique",
        )

    def test_etudiant_creation(self):
        self.assertEqual(self.etudiant.nom, "Test")
        self.assertEqual(self.etudiant.prenom, "User")
        self.assertTrue(self.etudiant.mdp.startswith('pbkdf2_'))
