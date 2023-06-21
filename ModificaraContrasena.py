import sys
import csv
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QPushButton, QMainWindow, QLineEdit, QDialog, QGridLayout, QMessageBox
from PyQt6.QtCore import Qt

def update_password_in_csv(username, new_password, csv_file):
    data = []
    with open(csv_file, "r", newline="") as csvfile:
        reader = csv.reader(csvfile, dialect="excel")
        for row in reader:
            data.append(row)
    for row in data:
        if row[2] == username:
            row[3] = new_password
            break
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, dialect="excel")
        writer.writerows(data)

class ModificarContraseña(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar Contraseña")

        ventanaGrande = QVBoxLayout()
        subVentana = QHBoxLayout()
        ventanaderecha = QVBoxLayout()
        self.lista = QListWidget()

        logo = QLabel(self)
        imagen = QPixmap(r"./logo.png")
        logo.setPixmap(imagen)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mc = QPushButton("Modificar Contraseña")
        volver = QPushButton("Volver")
        volver.clicked.connect(self.cerrar)
        mc.clicked.connect(self.modificar_contrasena)
        mc.clicked.connect(self.get_items)

        ventanaderecha.addWidget(mc)
        ventanaderecha.addWidget(volver)
        subVentana.addWidget(self.lista)

        ventanaGrande.addWidget(logo)

        ventana = QWidget()
        subVentana.addLayout(ventanaderecha)
        ventanaGrande.addLayout(subVentana)
        ventana.setLayout(ventanaGrande)
        self.setCentralWidget(ventana)

    def cargar_empleados_csv(self):
        with open("empleados.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  # Saltar la primera fila de encabezado
            for row in reader:
                empleado = row[0]
                clave = row[3]
                item = QListWidgetItem(empleado)
                item.setData(Qt.ItemDataRole.UserRole, clave)
                self.lista.addItem(item)

    def modificar_contrasena(self):
        items = self.lista.selectedItems()
        if items:
            username = items[0].text()
            clave = items[0].data(Qt.ItemDataRole.UserRole)
            modificar = Modificar(username, clave)
            modificar.exec()

    def cerrar(self):
        self.close()

    def get_items(self):
        items = self.lista.selectedItems()
        for item in items:
            print(item.text())

class Modificar(QDialog):
    def __init__(self, username, clave):
        super().__init__()
        self.setWindowTitle("Cambio de Contraseña")
        self.username = username
        self.clave = clave

        ventanita = QVBoxLayout()
        datos = QGridLayout()

        self.titulo = QLabel("Cambiar contraseña de usuario: " + self.username)
        self.contrasena = QLabel("Contraseña")
        self.confirmar_contrasena = QLabel("Confirmar contraseña")

        self.modificar_contrasena = QLineEdit()
        self.modificar_contrasena.setEchoMode(QLineEdit.EchoMode.Password)

        self.modificar_confirmar = QLineEdit()
        self.modificar_confirmar.setEchoMode(QLineEdit.EchoMode.Password)

        cambiar = QPushButton("Cambiar")
        cambiar.clicked.connect(self.igualdad)

        datos.addWidget(self.contrasena, 0, 0)
        datos.addWidget(self.confirmar_contrasena, 1, 0)
        datos.addWidget(self.modificar_contrasena, 0, 1)
        datos.addWidget(self.modificar_confirmar, 1, 1)

        ventanita.addWidget(self.titulo)
        ventanita.addLayout(datos)
        ventanita.addWidget(cambiar)

        self.setLayout(ventanita)

    def igualdad(self):
        a = self.modificar_contrasena.text()
        b = self.modificar_confirmar.text()
        c = a.replace(" ", "")
        if a == b:
            if c != "":
                QMessageBox.information(self, "Modificar contraseña", "Contraseña cambiada.")
                new_password = a
                csv_file = "empleados.csv"
                update_password_in_csv(self.username, new_password, csv_file)
                self.close()
            else:
                QMessageBox.information(self, "Modificar contraseña", "Contraseña vacía")
        else:
            QMessageBox.information(self, "Modificar contraseña", "Las contraseñas no coinciden.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ModificarContraseña()
    ventana.cargar_empleados_csv()
    ventana.show()
    sys.exit(app.exec())
