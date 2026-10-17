import csv
import os

from animal import Animal

class GestionZoo:

    def __init__(self, chemin_fichier_csv = "animaux.csv"):
        self.animaux = {}
        self.chemin_fichier_csv = chemin_fichier_csv
        self.charger_depuis_csv()

    def ajouter_animal(self, nouvel_animal):
        # ajouter un nouveau animal dans le dictionnaire en 0 seconde
        if nouvel_animal.identifiant in self.animaux:
            raise ValueError(f"Erreur: ID '{nouvel_animal.identifiant}' est deja utilize dans le zoo")

        self.animaux[nouvel_animal.identifiant]= nouvel_animal
        

    def supprimer_animal(self, identifiant):
        if identifiant in self.animaux:
            del self.animaux[identifiant]
            print(f"Animal ak ID {identifiant} est supprime")
            return True
        else:
            print(f"Il n'y a aucun animal dan la liste qui correspond a l'ID {identifiant}")
            return False

    def modifier_animal(self, identifiant, nouveau_nom, nouvelle_espece, nouvelle_age, nouveau_poids, nouveau_enclos, nouvelle_statut):
        animal = self.rechercher_par_id(identifiant)
        if animal:
            animal.modifier_info(nouveau_nom, nouvelle_espece, nouvelle_age, nouveau_poids, nouveau_enclos, nouvelle_statut)
            print(f"L'information de l'animal avec l'ID {identifiant}")
            return True
        else:
            print(f"Il n'y a auucun animal dans la liste qui correspond a l'ID {identifiant}")
            return False

    def rechercher_animal(self, recherche):
        resultats = []
        mot_cle = str(recherche).strip()
        mot_cle_lower = mot_cle.lower()

        if mot_cle in self.animaux:
            resultats.append(self.animaux[mot_cle])

        for animal in self.animaux.values():
            if (mot_cle_lower in animal.identifiant.lower() or 
                mot_cle_lower in animal.nom.lower() or 
                mot_cle_lower in animal.espece.lower()):
                if animal not in resultats:
                    resultats.append(animal)
        return resultats

    def rechercher_par_id(self, identifiant):
        # """Methode de service pour rechercher precisement une seule ID"""
        return self.animaux.get(identifiant)
    
    def affichier_animaux(self, limite = 20):
        """Affichier tous lea animaux dans le zoo"""
        if not self.animaux:
            return "Il n'y a aucau animaux dans le zoo pour le moment"

        total = len(self.animaux)
        for count, animal in enumerate(self.animaux.values()):
            if count >= limite:
                print(f"...avec {total - limite} autre animal dans le zoo")
                break
            animal.affichier_info()

    def doyen(self):
        # "Retourner l'animal qi est le plus age dans le zoo"
        if not self.animaux:
            return None
        return max(self.animaux.values(), key=lambda a: a.age)

    def plus_lourd(self):
        """Retourner l'animal le plus lourd dans le zoo"""
        if not self.animaux:
            return None
        return max(self.animaux.values(), key=lambda a: a.poids)
    
    def classer_animaux(self, par_critere = "age", inverse=True):
        """Trier les animaux par leur age ou par leur poids"""
        if par_critere == "poids":
            return sorted(self.animaux.values(), key= lambda a: a.poids, reverse=inverse)
        return sorted(self.animaux.values(), key= lambda a: a.age, reverse=inverse)
    
    def afficher_statistiques(self):
        # """Calculer et affichier la stat du zoo (total, age moyen, poids moyen)"""
        total = len(self.animaux)
        if total == 0:
            return("Statistique: le zoo est vide pour le moment")

        age_moyen = sum(a.age for a in self.animaux.values()) / total
        poids_moyen = sum(a.poids for a in self.animaux.values()) / total

        print("\n---STASISTIQUE DU ZOO---")
        print(f"Total des animaux: {total}")
        print(f"Age moyen: {age_moyen: .1} an")
        print(f"poids moyen: {poids_moyen: .1} kg")

    def charger_depuis_csv(self):
        """Lire le fichier CSV pour la rempli de self.liste_animaux"""
        if not os.path.exists(self.chemin_fichier_csv):
            return

        with open(self.chemin_fichier_csv, mode="r", encoding="utf-8") as fichier:
            reader = csv.DictReader(fichier)
            self.animaux = {}
            for ligne in reader:
                animal = Animal(
                    identifiant= ligne["identifiant"],
                    nom= ligne["nom"],
                    espece= ligne["espece"],
                    age= int(ligne["age"]),
                    poids= float(ligne["poids"]),
                    enclos= ligne["enclos"],
                    statut_sante= ligne["statut_sante"]
                )
                self.animaux[animal.identifiant] = animal

    def sauvegarder_dans_csv(self):
        # """Enregistrer tout la liste des animaux dans le fichier"""
        champs = ["identifiant", "nom", "espece", "age", "poids", "enclos", "statut_sante"]
        with open(self.chemin_fichier_csv, mode="w", newline="", encoding="utf-8") as fichier:
            lire = csv.DictWriter(fichier, fieldnames= champs)
            lire.writeheader()
            for animal in self.animaux.values():
                lire.writerow(animal.to_dict())
        print("Les donnees sont enregistres avec succes")