import sys
import os

# Ajouter la racine pour trouver tous les fichiers
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QTabWidget
)

from animal_dialog import AnimalDialog
from gestion_zoo import GestionZoo
from animal import Animal
from Onglet_statistique import OngletStatistiques
from Onglet_classement import OngletClassement

class MainWindow(QMainWindow):
    """Fenèt prensipal aplikasyon an"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SYSTEME DE GESTION DU ZOO")
        self.resize(850, 500)

        # Inisyalizasyon lojik metye a
        self.zoo = GestionZoo("zoo_donnees.csv")
        self.onglet_stat = OngletStatistiques(self.zoo)
        self.onglet_classement = OngletClassement(self.zoo)


        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tab_liste = QWidget()
        self.init_tab_liste()
        self.tabs.addTab(self.tab_liste, "Liste des animaux")
        self.tabs.addTab(self.onglet_stat, "Statistique")
        self.tabs.addTab(self.onglet_classement, "Classement")

        self.rafraichir_tableau()

    def init_tab_liste(self):
        layout = QVBoxLayout(self.tab_liste)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Nom", "Espece", "Age", "Poids", "Enclos", "Sante"])
        layout.addWidget(self.table)

        layout_bouttons = QHBoxLayout()
        self.btn_ajouter = QPushButton("Ajouter Animal")
        self.btn_modifier = QPushButton("Modifier Animal")
        self.btn_supprimer = QPushButton("Supprimer")

        layout_bouttons.addWidget(self.btn_ajouter)
        layout_bouttons.addWidget(self.btn_modifier)
        layout_bouttons.addWidget(self.btn_supprimer)
        layout.addLayout(layout_bouttons)

        # Koneksyon bouton yo ak bon fonksyon yo
        self.btn_ajouter.clicked.connect(self.ajouter_animal_ui)
        self.btn_modifier.clicked.connect(self.modifier_animal_ui)
        self.btn_supprimer.clicked.connect(self.supprimer_animal_ui)

    def rafraichir_tableau(self):
       self.table.setRowCount(0)  
       animaux_dict = self.zoo.animaux
       
       self.table.setRowCount(len(animaux_dict))
       for row_idx, animal in enumerate(animaux_dict.values()):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(animal.identifiant)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(animal.nom)))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(animal.espece)))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(animal.age)))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(animal.poids)))
            self.table.setItem(row_idx, 5, QTableWidgetItem(str(animal.enclos)))
            self.table.setItem(row_idx, 6, QTableWidgetItem(str(animal.statut_sante)))
 
            texte_age = "1 an" if animal.age == 1 else f"{animal.age} ans"
            texte_poids = f"{animal.poids} kg"
            self.table.setItem(row_idx, 3, QTableWidgetItem(texte_age))
            self.table.setItem(row_idx, 4, QTableWidgetItem(texte_poids))
            self.onglet_stat.rafraichir()
            self.onglet_classement.rafraichir_classement()

    def ajouter_animal_ui(self):
        dialog = AnimalDialog(self)
        if dialog.exec() == AnimalDialog.DialogCode.Accepted:
            data = dialog.recuper_donnees()
            if any(char.isdigit() for char in data["nom"]) or any(char.isdigit() for char in data["espece"]):
                QMessageBox.warning(self, "Attention", "Le nom et l'espèce ne doivent pas contenir de chiffres !")
                return
            try:
                nouvel_id = f"ANI-{len(self.zoo.animaux) + 1}"
                nouvel_animal = Animal(
                    nouvel_id, 
                    data["nom"], 
                    data["espece"],
                    int(data["age"]), 
                    float(data["poids"]), 
                    data["enclos"], 
                    data["statut_sante"]
                )
                self.zoo.ajouter_animal(nouvel_animal)
                self.zoo.sauvegarder_dans_csv()
                self.rafraichir_tableau()
                QMessageBox.information(self, "Succes", "Cet animal est ajoute avec succes")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Echec de l'ajout {str(e)}")

    def modifier_animal_ui(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Attention", "S'il vous plait, choisissez un animal dans le tableau pour le modifier.")
            return
        
        identifiant = self.table.item(selected_row, 0).text()
        animal_existant = self.zoo.rechercher_par_id(identifiant)
        if not animal_existant:
            return

        dialog = AnimalDialog(self, animal=animal_existant)
        if dialog.exec() == AnimalDialog.DialogCode.Accepted:
            data = dialog.recuper_donnees()
            try:
                self.zoo.modifier_animal(
                    identifiant, 
                    data["nom"], 
                    data["espece"],
                    int(data["age"]), 
                    float(data["poids"]),
                    data["enclos"], 
                    data["statut_sante"]
                )
                self.zoo.sauvegarder_dans_csv()
                self.rafraichir_tableau()
                QMessageBox.information(self, "Succes", "Animal modifie avec succes !")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Echec de la modification {str(e)}")

    def supprimer_animal_ui(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Attention", "S'il vous plait, choisissez un animal dans le tableau pour l'effacer")
            return

        identifiant = self.table.item(selected_row, 0).text()
        confirmation = QMessageBox.question(
            self, "Confirmation", f"Voulez-vous effacer l'animal avec l'ID '{identifiant}' ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if confirmation == QMessageBox.StandardButton.Yes:
            self.zoo.supprimer_animal(identifiant)
            self.zoo.sauvegarder_dans_csv()
            self.rafraichir_tableau()
            QMessageBox.information(self, "Succes", "Cet animal est efface avec succes")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = MainWindow()
    fenetre.show()
    sys.exit(app.exec())