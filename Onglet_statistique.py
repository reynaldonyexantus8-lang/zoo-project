from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

class OngletStatistiques(QWidget):
    def __init__(self, zoo):
        super().__init__()
        self.zoo = zoo
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.label_stats = QLabel("Chajman estatistik...")
        layout.addWidget(self.label_stats)

        self.btn_doyen = QPushButton("Afficher le doyen du zoo")
        self.btn_doyen.clicked.connect(self.afficher_doyen)
        layout.addWidget(self.btn_doyen)

        self.setLayout(layout)
        self.rafraichir()

    def rafraichir(self):
        animaux = list(self.zoo.animaux.values())
        total_animaux = len(animaux)
        
        if total_animaux > 0:
            ages = [a.age for a in animaux]
            poids = [a.poids for a in animaux]
            
            age_moyen = sum(ages) / total_animaux
            poids_moyen = sum(poids) / total_animaux
            
            age_max = max(ages)
            age_min = min(ages)
            poids_max = max(poids)
            poids_min = min(poids)
            
            sante_counts = {"Bon": 0, "Sous suveillance": 0, "Malade": 0}
            espece_counts = {}
            
            for a in animaux:
                if a.statut_sante in sante_counts:
                    sante_counts[a.statut_sante] += 1
                espece = a.espece
                espece_counts[espece] = espece_counts.get(espece, 0) + 1
        else:
            age_moyen = poids_moyen = age_max = age_min = poids_max = poids_min = 0
            sante_counts = {"Bon": 0, "Sous surveillance": 0, "Malade": 0}
            espece_counts = {}

        texte_stats = f"""
        <span style="color: #2E7D32; font-weight: bold;"> QUANTITE TOTAL D'ANIMAUX:</span> {total_animaux}<br>
        <span style="color: #1565C0;"> Age moyen:</span> {age_moyen:.2f} ans<br>
        <span style="color: #1565C0;"> Poids moyen:</span> {poids_moyen:.2f} kg<br>
        <span style="color: #EF6C00;"> age max / min:</span> {age_max} ans / {age_min} an<br>
        <span style="color: #EF6C00;"> Poids max / min:</span> {poids_max} kg / {poids_min} kg<br><br>
        
        <span style="color: #6A1B9A; font-weight: bold;"> STATUT DE SANTE:</span><br>
        - Bon: {sante_counts['Bon']}<br>
        - Sous suveillance: {sante_counts['Sous suveillance']}<br>
        - Malade: {sante_counts['Malade']}<br><br>
        
        <span style="color: #00838F; font-weight: bold;"> Nombre d'animaux par espèce:</span>
        """
        for esp, count in espece_counts.items():
            texte_stats += f"<br>- {esp}: {count}"

        self.label_stats.setText(texte_stats)

    def afficher_doyen(self):
        animaux = list(self.zoo.animaux.values())
        if not animaux:
            QMessageBox.information(self, "Doyen du zoo", "Il n'y en a pas pour le moment")
            return

        doyen = max(animaux, key=lambda a: a.age)
        QMessageBox.information(self, "Doyen du zoo", f"L'animal le plus grand du zoo est: \nNom: {doyen.nom} \nEspece: {doyen.espece} \nAge: {doyen.age} ans")