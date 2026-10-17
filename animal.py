class Animal:

    def __init__(self, identifiant, nom, espece, age, poids, enclos, statut_sante):
        # Validons les donnees avant l'enregistrement
        self.valider_donnees(nom, espece, age, poids, enclos, statut_sante)

        # Enregistrement
        self.identifiant = identifiant
        self.nom = nom
        self.espece = espece
        self.age = age
        self.poids = poids
        self.enclos = enclos
        self.statut_sante = statut_sante

    @staticmethod
    def valider_donnees(nom, espece, age, poids, enclos, statut_sante):

        if not nom or not espece or not enclos:
            raise ValueError("Le nom, l'espece et l'enclos ne doivent pas etre vide")

        if not int((0<= age <=100)):
            raise ValueError("L'age doit etre compris entre 0 et 100 ans")

        if float(poids <=0):
            raise ValueError("Le poids doit etre stictement superieur a 0")

        status_autorisees = ["Bon", "Sous suveillance", "Malade"]
        if statut_sante not in status_autorisees:
            raise ValueError(f"La statue de sante doit etre une de ces options: {status_autorisees}")

    def modifier_info(self, nom, espece, age, poids, enclos, statut_sante):
        self.valider_donnees(nom, espece, age, poids, enclos, statut_sante)
        self.nom = nom
        self.espece = espece
        self.age = age
        self.poids = poids
        self.enclos = enclos
        self.statut_sante = statut_sante

    def est_senior(self, seuil=15):
        return self.age >= seuil

    def afficher_infos(self):
        print(f"[{self.identifiant}] {self.nom} ({self.espece}) - {self.age} an(s), {self.poids} kg | Sante: {self.statut_sante}")

    def to_dict(self):
        return{
            "identifiant": self.identifiant,
            "nom": self.nom,
            "espece": self.espece,
            "age": self.age,
            "poids": self.poids,
            "enclos": self.enclos,
            "statut_sante": self.statut_sante
        }