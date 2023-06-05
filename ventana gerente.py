import sys
from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class VentanaPrincipal(QWidget):
    def __init__(self, nombre_empresa):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión")
        self.setWindowIcon(QIcon(r".\logo.png"))  

        # Logo y nombre 
        self.logo_lbl = QLabel()
        self.logo_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo_pixmap = QPixmap(r".\logo.png")
        self.logo_lbl.setPixmap(self.logo_pixmap)

        self.empresa_lbl = QLabel(nombre_empresa)
        self.empresa_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empresa_lbl.setStyleSheet("font-size: 20px; font-weight: bold;")

        # bienvenida
        self.bienvenida_lbl = QLabel("Bienvenido/a, [Nombre]")
        self.bienvenida_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bienvenida_lbl.setFont(QFont("Arial", 16))

        # Botones
        self.registrar_btn = QPushButton("Registrar nuevo empleado")
        self.despedir_btn = QPushButton("Desvincular empleado")
        self.crear_modificar_btn = QPushButton("Crear o modificar turnos")
        self.modificar_contrasena_btn = QPushButton("Modificar contraseña de empleado")

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

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal("Empresa")
    ventana.show()
    sys.exit(app.exec())
