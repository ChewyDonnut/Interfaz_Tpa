from ModificarContrasena import ModificarContraseña
import sys
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow
from RegistrarEmpleadoTurnos import VentanaRegistro
from VentanaDesvincular import Desvincular 
from RegistrarEmpleadoTurnos import VentanaPrincipal
class VentanaGerente(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión")
        self.setWindowIcon(QIcon(r".\logo.png"))  
        self.ventana_registrar = VentanaRegistro()
        self.ventana_desvincular = Desvincular()
        self.ventana_modificar = VentanaPrincipal()
        # Logo y nombre 
        self.logo_lbl = QLabel()
        self.logo_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_pixmap = QPixmap(r".\logo.png")
        self.logo_lbl.setPixmap(self.logo_pixmap)

        self.empresa_lbl = QLabel("Empresa")
        self.empresa_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empresa_lbl.setStyleSheet("font-size: 20px; font-weight: bold;")

        # bienvenida
        self.bienvenida_lbl = QLabel("Bienvenido/a, [Nombre]")
        self.bienvenida_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bienvenida_lbl.setFont(QFont("Arial", 16))

        # Botones
        self.registrar_btn = QPushButton("Registrar nuevo empleado")
        self.despedir_btn = QPushButton("Desvincular empleado")
        self.despedir_btn.clicked.connect(self.desvincular)
        self.crear_modificar_btn = QPushButton("Crear o modificar turnos")
        self.modificar_contrasena_btn = QPushButton("Modificar contraseña de empleado")
        self.modificar_contrasena_btn.clicked.connect(self.modificar)

        self.registrar_btn.clicked.connect(lambda: self.ventana_registrar.show())
        self.despedir_btn.clicked.connect(lambda: self.ventana_desvincular.show())
        self.crear_modificar_btn.clicked.connect(lambda: self.ventana_modificar.show())
        # Diseño de la ventana
        layout = QVBoxLayout()
        layout.addWidget(self.logo_lbl)
        layout.addWidget(self.empresa_lbl)
        layout.addWidget(self.bienvenida_lbl)

        layout_botones1 = QHBoxLayout()
        layout_botones1.addWidget(self.registrar_btn)
        layout_botones1.addWidget(self.despedir_btn)

        layout_botones2 = QHBoxLayout()
        layout_botones2.addWidget(self.crear_modificar_btn)
        layout_botones2.addWidget(self.modificar_contrasena_btn)

        layout.addLayout(layout_botones1)
        layout.addLayout(layout_botones2)

        layout_widget = QWidget()
        layout_widget.setLayout(layout)

        self.setCentralWidget(layout_widget)

    def modificar(self):
        self.modi=ModificarContraseña()
        self.modi.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaGerente()
    ventana.show()
    sys.exit(app.exec())