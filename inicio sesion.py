import sys
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class VentanaInicioSesion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de sesión")
        self.setWindowIcon(QIcon(r"C:\Users\luisr\OneDrive\Escritorio\logo empresa.png"))
        # Logo y nombre
        self.etiqueta_logo = QLabel()
        self.etiqueta_logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pix_map_logo = QPixmap((r"C:\Users\luisr\OneDrive\Escritorio\logo empresa.png"))
        self.etiqueta_logo.setPixmap(self.pix_map_logo)

        self.etiqueta_empresa = QLabel("Empresa")
        self.etiqueta_empresa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.etiqueta_empresa.setStyleSheet("font-size: 20px; font-weight: bold;")

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
        layout.addWidget(self.etiqueta_logo)
        layout.addWidget(self.etiqueta_empresa)
        layout.addWidget(self.etiqueta_usuario)
        layout.addWidget(self.entrada_usuario)
        layout.addWidget(self.etiqueta_contrasena)
        layout.addWidget(self.entrada_contrasena)
        layout.addWidget(self.boton_inicio_sesion)

        self.setLayout(layout)

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.text()
        contrasena = self.entrada_contrasena.text()

       
        print("Inicio de sesión completado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaInicioSesion()
    ventana.show()
    sys.exit(app.exec())