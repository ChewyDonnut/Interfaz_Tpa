import sys
import typing
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow,QListWidget,QHBoxLayout,QDialog,QGridLayout,QMessageBox

class Desvincular(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar Contraseña")

    #ventanas
        #ventana principal
        ventanaGrande=QVBoxLayout()# integra logo  y subventana
        subVentana=QHBoxLayout()#integra lista a la derecha y ventana derecha
        ventanaderecha=QVBoxLayout()#incluye dos botones derechos
        self.lista=QListWidget()#lista
      
        
        #logo
        logo=QLabel(self)#cambiar al centro
        imagen = QPixmap(r"./logo.png")   
        logo.setPixmap(imagen)
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #botones
        mc=QPushButton("Desvincular")
        volver=QPushButton("volver")
        #volver.clicked.connect(self.cerrar)#creo que se puede achicar la funcion
        mc.clicked.connect(self.emergente_desvincular)
       

        #asignar widgets
        ventanaderecha.addWidget(mc)
        ventanaderecha.addWidget(volver)
        subVentana.addWidget(self.lista)
        
        ventanaGrande.addWidget(logo)
        

        #asignar ventanas
        ventana=QWidget()
        subVentana.addLayout(ventanaderecha)
        ventanaGrande.addLayout(subVentana)
        ventana.setLayout(ventanaGrande)
        self.setCentralWidget(ventana)
    def emergente_desvincular(self):
        ventanita=ConfirmarDesvincular()
        ventanita.exec()
class ConfirmarDesvincular(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desvincular Empleado")

        #ventana
        ventanita=QVBoxLayout()

        #grid
        datos=QGridLayout()
        
        #informacion de pantalla
        self.titulo=QLabel("Desvinculacion de usuario")#aqui va el nombre de la persona tambien 
        self.usuario=QLabel("usuario")
        self.confirmar_usuario=QLabel("confirmar usuario")
        #datoas a ingresar
        self.eliminar_usuario=QLineEdit("")#primera contraseña
        self.eliminar_confirmar=QLineEdit("")#segunda contraseña
        #boton
        cambiar=QPushButton("Desvincular")
        cambiar.clicked.connect(self.confirmacion)
        #asignar las al grid
        datos.addWidget(self.usuario,0,0)
        datos.addWidget(self.confirmar_usuario,1,0)
        datos.addWidget(self.eliminar_usuario,0,1)
        datos.addWidget(self.eliminar_confirmar,1,1)
        
        ventanita.addWidget(self.titulo)
        ventanita.addLayout(datos)
        ventanita.addWidget(cambiar)
        self.setLayout(ventanita)
    def confirmacion(self):
        a=self.eliminar_confirmar.text()
        b=self.eliminar_usuario.text()
        c=a.replace(" ","")
        if a==b:
            if c!="":         
                QMessageBox.information(self, "Empleados (Nombre Empresa)", "Empleado registrado exitosamente.")
                self.close()
            else:
               QMessageBox.information(self, "Empleados (Nombre Empresa)", "contrasña vacia")

        else:
            QMessageBox.information(self, "Empleados (Nombre Empresa)", "Contraseñas diferentes.")
            

if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Desvincular()
    ventana.show()
    sys.exit(app.exec())