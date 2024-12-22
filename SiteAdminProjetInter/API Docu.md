# Documentation des APIs

## **Résumé général**

Ce projet fournit des **APIs REST en lecture seule** pour interagir avec les données d'un système de gestion scolaire. Les APIs permettent de **consulter des informations** sur :

- Les étudiants,
- Les professeurs,
- Les salles,
- Les cours,
- Les absences,
- Les notes,
- Les incidents signalés,
- Les inscriptions aux cours,
- Les plannings.

Toutes les données sont disponibles via des endpoints sécurisés et structurés, offrant des réponses au format JSON.

---

## **Endpoints disponibles**

(Un endpoint en API REST est une URL spécifique où un client peut envoyer une requête pour interagir avec une ressource (comme lire, créer, mettre à jour ou supprimer des données).)

| Ressource        | Description                   | Méthode HTTP | URL                                       |
| ---------------- | ----------------------------- | ------------ | ----------------------------------------- |
| **Étudiants**    | Liste de tous les étudiants   | `GET`        | `http://127.0.0.1:8000/api/etudiants/`    |
| **Professeurs**  | Liste de tous les professeurs | `GET`        | `http://127.0.0.1:8000/api/professeurs/`  |
| **Salles**       | Liste de toutes les salles    | `GET`        | `http://127.0.0.1:8000/api/salles/`       |
| **Cours**        | Liste de tous les cours       | `GET`        | `http://127.0.0.1:8000/api/cours/`        |
| **Absences**     | Liste des absences            | `GET`        | `http://127.0.0.1:8000/api/absences/`     |
| **Notes**        | Liste des notes globales      | `GET`        | `http://127.0.0.1:8000/api/notes/`        |
| **Incidents**    | Liste des incidents signalés  | `GET`        | `http://127.0.0.1:8000/api/incidents/`    |
| **Inscriptions** | Liste des inscriptions        | `GET`        | `http://127.0.0.1:8000/api/inscriptions/` |
| **Plannings**    | Liste des plannings des cours | `GET`        | `http://127.0.0.1:8000/api/plannings/`    |

---

## **Exemple d’utilisation des APIs**

### **Étudiants**

- **Tous les étudiants** :  
    `GET http://127.0.0.1:8000/api/etudiants/`
    
- **Filtres disponibles** :
    
    - Par département : `?departement=Informatique`
    - Par statut (actif/inactif) : `?statut=true`
    - Recherche textuelle : `?search=nom_ou_email`

### **Professeurs**

- **Tous les professeurs** :  
    `GET http://127.0.0.1:8000/api/professeurs/`
    
- **Recherche textuelle** :
    
    - Recherche par nom ou email : `?search=dupont`

### **Salles**

- **Toutes les salles** :  
    `GET http://127.0.0.1:8000/api/salles/`
    
- **Filtres disponibles** :
    
    - Par département : `?departement=Physique`
    - Salles disponibles : `?statut=true`

### **Cours**

- **Tous les cours** :  
    `GET http://127.0.0.1:8000/api/cours/`
    
- **Recherche textuelle** :
    
    - Recherche par nom de cours : `?search=math`