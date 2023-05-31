import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QVBoxLayout, QDialog, QHBoxLayout, QLineEdit

class HorasTrabajadas(QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(340,340)
        self.setWindowTitle("Horas trabajadas")
        self.setModal(True)
        #Elementos
        # Logo
        logo = QLabel("Empresa")
        self.texto1 = QLabel("Horas trabajadas")
        self.texto2 = QLabel("Semana")
        self.texto3 = QLabel("Mes")
        self.texto2_horas = QLabel("0")
        self.texto3_horas = QLabel("0")
        #centrar labels
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto2_horas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.texto3_horas.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton_volver = QPushButton("Volver al menu")

        #Conectar botones
        self.boton_volver.clicked.connect(self.hide)

        #Contenedores
        textos = QGridLayout()
        textos.addWidget(self.texto1,0,1)
        textos.addWidget(self.texto2,1,0)
        textos.addWidget(self.texto3,1,2)
        textos.addWidget(self.texto2_horas,2,0)
        textos.addWidget(self.texto3_horas,2,2)

        textos_widget = QWidget()
        textos_widget.setLayout(textos)

        contenedor_principal = QVBoxLayout()
        contenedor_principal.addWidget(logo)
        contenedor_principal.addWidget(textos_widget)
        contenedor_principal.addWidget(self.boton_volver)
        self.setLayout(contenedor_principal)

class VerTurnos(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Turnos")
        self.setFixedSize(700,430)
        self.setModal(True)
        #Elementos
        logo = QLabel("Empresa")
        self.tabla = QLabel("test")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabla.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.boton_volver = QPushButton("Volver al menu")
        #Conectar botones
        self.boton_volver.clicked.connect(self.hide)
        
        #Contenedores
        contenedor = QVBoxLayout()
        contenedor.addWidget(logo)
        contenedor.addWidget(self.tabla)
        contenedor.addWidget(self.boton_volver)

        self.setLayout(contenedor)

class IngresoSalida(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Marcar Ingreso o Salida")
        self.setFixedSize(430,430)
        self.setModal(True)

        #Elementos
        logo = QLabel("Empresa")
        self.boton_ingreso = QPushButton("Ingreso")
        self.boton_salida = QPushButton("Salida")
        self.boton_volver = QPushButton("Volver al menu")
        
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Conectar botones
        self.boton_volver.clicked.connect(self.hide)
        #Contenedores
        botones = QHBoxLayout()
        botones.addWidget(self.boton_ingreso)
        botones.addWidget(self.boton_salida)

        botones_widget = QWidget()
        botones_widget.setLayout(botones)

        contenedor = QVBoxLayout()
        contenedor.addWidget(logo)
        contenedor.addWidget(botones_widget)
        contenedor.addWidget(self.boton_volver)

        self.setLayout(contenedor)
        

class CambiarContrasena(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cambiar contraseña")
        self.setFixedSize(340,204)
        self.setModal(True)
        #Elementos
        self.texto = QLabel("Cambiar contraseña")
        self.texto_contrasena = QLabel("Contraseña")
        self.texto_confirmar = QLabel("Confirmar contraseña")
        self.entrada_contrasena = QLineEdit()
        self.entrada_confirmar = QLineEdit()
        
        self.entrada_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.entrada_confirmar.setEchoMode(QLineEdit.EchoMode.Password)

        self.boton_confirmar = QPushButton("Confirmar")

        #Contenedores
        entradas = QGridLayout()
        entradas.addWidget(self.texto_contrasena,0,0)
        entradas.addWidget(self.entrada_contrasena,0,1)
        entradas.addWidget(self.texto_confirmar,1,0)
        entradas.addWidget(self.entrada_confirmar,1,1)

        entradas_widget = QWidget()
        entradas_widget.setLayout(entradas)
        
        contenedor = QVBoxLayout()
        contenedor.addWidget(self.texto)
        contenedor.addWidget(entradas_widget)
        contenedor.addWidget(self.boton_confirmar)

        self.setLayout(contenedor)

class VentanaEmpleado(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(530,610)
        self.setWindowTitle("Ventana Empleado")
        #ventanas
        self.horas_trabajadas = HorasTrabajadas()
        self.ver_turnos = VerTurnos()
        self.ingreso_salida = IngresoSalida()
        self.cambiar_con = CambiarContrasena()

        #Elementos
        logo = QLabel("Empresa")
        self.bienvenida = QLabel(f"Bienvenido: <nombre> Area: <rol>")
        #centrar textos
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton_cambiar = QPushButton("Cambiar contraseña")
        self.boton_ver_turnos = QPushButton("Ver turnos")
        self.boton_horas_trabajadas = QPushButton("Horas trabajadas")
        self.boton_ingsal = QPushButton("Ingreso/Salida")

        self.lista_pendientes = QLabel()

        #conectar botones
        self.boton_horas_trabajadas.clicked.connect(lambda: self.desplegar(0))
        self.boton_ver_turnos.clicked.connect(lambda: self.desplegar(1))
        self.boton_ingsal.clicked.connect(lambda: self.desplegar(2))
        self.boton_cambiar.clicked.connect(lambda: self.desplegar(3))

        #Contenedores
        botones = QGridLayout()
        botones.addWidget(self.boton_cambiar,0,1)
        botones.addWidget(self.boton_ver_turnos,1,0)
        botones.addWidget(self.boton_horas_trabajadas,1,1)
        botones.addWidget(self.boton_ingsal,1,2)
        
        botones_widget = QWidget()
        
        botones_widget.setLayout(botones)

        contenedor = QVBoxLayout()
        contenedor.addWidget(logo)
        contenedor.addWidget(self.bienvenida)
        contenedor.addWidget(botones_widget)
        contenedor.addWidget(self.lista_pendientes)

        self.setLayout(contenedor)
    
    def desplegar(self,id:int):
        #id 0 para horas trabajadas
        if id == 0:
            if self.horas_trabajadas.isHidden():
                self.horas_trabajadas.show()
            else:
                self.horas_trabajadas.hide()
        #id 1 para ver turnos
        if id == 1:
            if self.ver_turnos.isHidden():
                self.ver_turnos.show()
            else:
                self.ver_turnos.hide()
        #id 2 para ingreso/salida
        if id == 2:
            if self.ingreso_salida.isHidden():
                self.ingreso_salida.show()
            else:
                self.ingreso_salida.hide()
        #id 3 para cambiar contraseña
        if id == 3:
            if self.cambiar_con.isHidden():
                self.cambiar_con.show()
            else:
                self.cambiar_con.hide()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaEmpleado()
    ventana.show()
    app.exec()