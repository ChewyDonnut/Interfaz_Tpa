import sys
import csv
from VentanaEmpleado import VentanaEmpleado
from VentanaGerente import VentanaGerente
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from Gerente import Gerente
from Empleado import Empleado

usuarios_contrasenas = {}

with open('empleados.csv', newline='') as archivo:
    lector_csv = csv.reader(archivo, delimiter=',')
    next(lector_csv)  # Ignorar la primera línea de encabezados
    for fila in lector_csv:
        nombre = fila[0].strip()
        rol = fila[1].strip()
        usuario = fila[2].strip()
        contrasena = fila[3].strip()
        if rol == "Gerente":
            usuarios_contrasenas[usuario] = Gerente(nombre, rol, usuario, contrasena)
        else:
            usuarios_contrasenas[usuario] = Empleado(nombre, rol, usuario, contrasena)

class VentanaInicioSesion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.ventana_gerente = VentanaGerente()
        self.ventana_empleado = VentanaEmpleado()

        self.nombre_usuario = ""
        
        
        logo = QLabel(self)
        imagen = QPixmap(r"logo.png")
        logo.setPixmap(imagen)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # inicio de sesión
        self.etiqueta_usuario = QLabel("Usuario:")
        self.entrada_usuario = QLineEdit()
        self.etiqueta_contrasena = QLabel("Contraseña:")
        self.entrada_contrasena = QLineEdit()
        self.entrada_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.boton_inicio_sesion = QPushButton("Iniciar sesión")
        self.boton_inicio_sesion.clicked.connect(self.iniciar_sesion)

        # Diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(logo)
        layout.addWidget(self.etiqueta_usuario)
        layout.addWidget(self.entrada_usuario)
        layout.addWidget(self.etiqueta_contrasena)
        layout.addWidget(self.entrada_contrasena)
        layout.addWidget(self.boton_inicio_sesion)

        self.setLayout(layout)

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.text()
        contrasena = self.entrada_contrasena.text()
        if usuario in usuarios_contrasenas:
            empleado = usuarios_contrasenas[usuario]
            if contrasena == empleado.getContrasena():
                if empleado.getRol() == "Gerente":
                    print("Inicio de sesión completado como Gerente")
                    self.ventana_gerente.show()
                    self.hide()
                else:
                    print("Inicio de sesión completado como Empleado")
                    ventana_empleado = VentanaEmpleado(empleado.getNombre())
                    ventana_empleado.show()
                    self.hide()
            else:
                QMessageBox.warning(self, "Error", "Contraseña incorrecta")
        else:
            QMessageBox.warning(self, "Error", "Usuario incorrecto")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaInicioSesion()
    ventana.show()
    sys.exit(app.exec())
