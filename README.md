# test-positionnement-django


# Test de positionnement – Django

Ce dépôt regroupe les exercices réalisés dans le cadre du test de positionnement, organisés par thème.

## Structure du dépôt

```
.
├── html/
│   └── listel_livre.html      # Page HTML/CSS/JS - liste de livres avec recherche
├── Python/
│   └── gestion_livres.py      # Programme de gestion de bibliothèque (POO)
├── uml/
│   ├── diagramme_classes.png  # Diagramme de classes - système de réservation de salles
│   └── cas_utilisation.png    # Diagramme de cas d'utilisation - système de réservation de salles
└── README.md
```

## Contenu et utilisation

### `html/listel_livre.html`

Page web statique (HTML/CSS/JS natif, sans framework) affichant une liste de livres sous forme de cartes, avec un champ de recherche qui filtre les résultats en temps réel selon le titre.

**Pour l'utiliser** : ouvrir le fichier directement dans un navigateur (double-clic sur le fichier, ou clic droit → Ouvrir avec → navigateur).

### `Python/gestion_livres.py`

Programme en ligne de commande illustrant la programmation orientée objet à travers deux classes :
- `Livre` : titre, auteur, année, disponibilité, avec les méthodes `emprunter()` et `retourner()`.
- `Bibliotheque` : gère une collection de `Livre` (ajout, recherche par auteur, livres disponibles, statistiques).

**Pour l'exécuter** :
```bash
python3 Python/gestion_livres.py
```
Le programme demande le nom de la bibliothèque puis les informations de 5 livres (titre, auteur, année, disponibilité), emprunte automatiquement 2 livres et en retourne 1, puis affiche les statistiques, les livres disponibles et permet une recherche par auteur.

### `uml/`

Modélisation UML d'un système de réservation de salles de réunion :

- **diagramme_classes.png** : classes `Employe`, `Administrateur` (hérite d'`Employe`), `Salle` et `Reservation`, avec leurs attributs, méthodes et relations (multiplicités incluses).
- **cas_utilisation.png** : cas d'utilisation du système — créer une réservation (Employé), valider/rejeter une réservation et ajouter/supprimer une salle (Administrateur).

Diagrammes réalisés avec [Dia](http://dia-installer.de/) ; seuls les exports PNG sont versionnés ici.
