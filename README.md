#  Système de Gestion de Zoo (Zoo Management System)

Un système complet de gestion de zoo développé en **Python 3** avec une interface graphique moderne bâtie sur **PyQt6** et une persistence de données basée sur des fichiers **CSV**.

---

##  Présentation du Projet

Ce projet a été conçu dans le cadre académique pour démontrer la mise en œuvre des principes d'orientation objet, de la gestion d'interfaces graphiques (GUI), de la persistence de données locales et de la structuration modulaire d'un code Python.

L'application permet d'administrer facilement les animaux d'un zoo à travers une interface à onglets intuitive pour suivre la santé, l'emplacement (enclos), les statistiques globales ainsi que les classements des animaux.

---

##  Fonctionnalités Principales

1. **Gestion des Animaux (CRUD)**:
   - Ajout: Saisie d'un nouvel animal via un formulaire contextuel (`AnimalDialog`).
   - Modification: Mise à jour des informations avec protection de l'identifiant unique (`setReadOnly`).
   - Suppression: Retrait sécurisé avec demande de confirmation.
   - Affichage : Tableau dynamique récapitulant les informations clés.

2. **Statistiques en Temps Réel** :
   - Calcul de l'effectif total, de l'âge moyen et du poids moyen.
   - Identification des valeurs extrêmes (âges et poids min/max).
   - Répartition par statut de santé (`Bon`, `Sous surveillance`, `Malade`).
   - Nombre d'animaux par espèce et identification du doyen du zoo.

3. **Classement et Tri Dynamique** :
   - Tri interactif par "Âge" ou par "Poids".
   - Inverseur d'ordre de tri (croissant / décroissant) à l'aide de fonctions `lambda`.

4. **Persistence des Données** :
   - Sauvegarde et chargement automatiques à partir d'un fichier CSV (`zoo_donnees.csv`) via `csv.DictReader` et `csv.DictWriter`.

---

##  Architecture du Code et Structure des Modules

| Fichier | Rôle / Description |
| :--- | :--- |
| `animal.py` | Modèle de données (Classe `Animal`) représentant un animal et gérant la conversion en dictionnaire (`to_dict`). |
| `gestion_zoo.py` | Logique métier (Classe `GestionZoo`) : opérations CRUD, recherche par ID, lecture et écriture CSV. |
| `animal_dialog.py` | Formulaire modal (`QDialog`) pour la saisie et la modification contrôlée des données d'un animal. |
| `Onglet_statistique.py` | Interface affichant les métriques globales et les indicateurs clés sous forme HTML enrichie. |
| `Onglet_classement.py` | Interface graphique dédiée au tri et au classement dynamique selon différents critères. |
| `main_window.py` | Fenêtre principale (`QMainWindow`) orchestrant l'ensemble des onglets et l'interaction globale. |

---

##  Configuration de l'Environnement et Enregistrement

## Préréquis
- Python 3.10+ installé.

###  Création et activation de l'environnement virtuel (`venv`)

## Installation des dependances
- pip install -r requirements.txt
## Contenu du fichier requirements.txt
- PyQt6==6.4.0

**Sur Windows** :
python -m venv venv
venv\Scripts\activate

### Lancement de l'application
Pour exécuter l'application, lancez la commande suivante depuis la racine du projet:
"python main_window.py"

Vous pouvez aussi consulter ce projet sur ma page [GitHub](https://github.com/reynaldonyexantus8-lang/zoo-project)