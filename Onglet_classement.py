from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QTableWidget, QTableWidgetItem

class OngletClassement(QWidget):
    def __init__(self, zoo):
        super().__init__()
        self.zoo = zoo
        self.ordre_ascendant = True  # Vre vle di soti nan pi piti al nan pi gwo
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Layout anlè a pou kontwòl yo (ComboBox ak Bouton)
        top_layout = QHBoxLayout()
        
        self.combo_critere = QComboBox()
        self.combo_critere.addItem("Age")
        self.combo_critere.addItem("Poids")
        # Konekte lè itilizatè a chanje kritè a pou l rafrechi tablo a
        self.combo_critere.currentIndexChanged.connect(self.rafraichir_classement)
        
        self.btn_inverser = QPushButton("Inverser l'ordre")
        self.btn_inverser.clicked.connect(self.inverser_ordre)

        top_layout.addWidget(self.combo_critere)
        top_layout.addWidget(self.btn_inverser)
        layout.addLayout(top_layout)

        # Tablo pou afiche bèt yo
        self.table_classement = QTableWidget()
        self.table_classement.setColumnCount(3)
        self.table_classement.setHorizontalHeaderLabels(["Nom", "Espèce", "Valeur"])
        layout.addWidget(self.table_classement)

        self.setLayout(layout)
        self.rafraichir_classement()

    def inverser_ordre(self):
        # Chanje ant True ak False
        self.ordre_ascendant = not self.ordre_ascendant
        self.rafraichir_classement()

    def rafraichir_classement(self):
        animaux = list(self.zoo.animaux.values())
        critere = self.combo_critere.currentText()

        # Triye bèt yo baze sou kritè a (Laj oswa Pwa)
        if critere == "age":
            animaux.sort(key=lambda a: a.age, reverse=not self.ordre_ascendant)
        else:
            animaux.sort(key=lambda a: a.poids, reverse=not self.ordre_ascendant)

        # Afiche nan tablo a
        self.table_classement.setRowCount(len(animaux))
        for row, a in enumerate(animaux):
            self.table_classement.setItem(row, 0, QTableWidgetItem(a.nom))
            self.table_classement.setItem(row, 1, QTableWidgetItem(a.espece))
            
            if critere == "Age":
                v = "an" if a.age ==1 else "ans"
                valeur = f"{a.age} {v}"
            else:
                valeur = f"{a.poids} kg"
            self.table_classement.setItem(row, 2, QTableWidgetItem(valeur))