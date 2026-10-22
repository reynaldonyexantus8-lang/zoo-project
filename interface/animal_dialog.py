from PyQt6.QtWidgets import(
    QDialog, 
    QLineEdit,
    QComboBox,
    QFormLayout,
    QPushButton
)

class AnimalDialog(QDialog):

    def __init__(self, parent = None, animal = None):
        super().__init__(parent)
        self.setWindowTitle("Form Animal")
        self.setFixedSize(300, 350)

        self.animal_modifie = animal

        layout = QFormLayout(self)

        self.input_id = QLineEdit()
        self.input_nom = QLineEdit()
        self.input_espece = QLineEdit()
        self.input_age = QLineEdit()
        self.input_poids = QLineEdit()
        self.input_enclos = QLineEdit()
        self.input_statut = QComboBox()
        self.input_statut.addItems(["Bon", "Sous suveillance", "Malade"])

        layout.addRow("Non:", self.input_nom)
        layout.addRow("Espece:", self.input_espece)
        layout.addRow("Age:", self.input_age)
        layout.addRow("Poids:", self.input_poids)
        layout.addRow("Enclos:", self.input_enclos)
        layout.addRow("Statut Sante:", self.input_statut)

        self.btn_valider = QPushButton("Enregistrer")
        self.btn_valider.clicked.connect(self.accept)
        layout.addRow(self.btn_valider)

        if self.animal_modifie:
            self.input_id.setText(self.animal_modifie.identifiant)
            self.input_id.setReadOnly(True)
            self.input_nom.setText(self.animal_modifie.nom)
            self.input_espece.setText(self.animal_modifie.espece)
            self.input_age.setText(str(self.animal_modifie.age))
            self.input_poids.setText(str(self.animal_modifie.poids))
            self.input_enclos.setText(self.animal_modifie.enclos)
            self.input_statut.setCurrentText(self.animal_modifie.statut_sante)

    def recuper_donnees(self):
        return{
            "identifiant": self.input_id.text().strip(),
            "nom": self.input_nom.text().strip(),
            "espece": self.input_espece.text().strip(),
            "age": self.input_age.text().strip(),
            "poids": self.input_poids.text().strip(),
            "enclos": self.input_enclos.text().strip(),
            "statut_sante": self.input_statut.currentText()
        }