from animal import Animal
from gestion_zoo import GestionZoo

def executer_zoo():
    print("---COMMENCEMENT DE L'EXECUTION---")

    zoo = GestionZoo("zoo_donnees.csv")

    print(f"\nMaintemnant, il y a {len(zoo.animaux)} animaux dans le systeme")

    nouveau_id = "A999"
    if nouveau_id not in zoo.animaux:
        a = Animal(nouveau_id, "Kala", "Tigre", 4, 150.0, "Zone B", "Bon")
        zoo.ajouter_animal(a)
        print(f"le nouveau animal ({a.nom}) est ajoute")

    # Tester la recherche
    print("\n---TEST DU RECHERCHE---")
    recherche = input("Taper le nom ou l'ID  de l'animal:")
    if recherche.strip():
        resultats = zoo.rechercher_animal(recherche)
        if resultats:
            for r in resultats:
                print(f"Trouve: {r.nom}, Enclos: {r.enclos}")
        else:
            print("Il 'y a aucun resultat pour cet animal")

    # Statistique
    print("\n---STATISTIQUES---")
    zoo.afficher_statistiques()

    doyen = zoo.doyen()
    if doyen:
        print(f"Le doyen du zoo est : {doyen.nom} ({doyen.age} an)")

    # Enregistrement dans le fichier csv
    zoo.sauvegarder_dans_csv()
    print("\n Tous les donnees sont sauvegarder dans le fichier")

if __name__ == "__main__":
    executer_zoo()