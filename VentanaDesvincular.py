import sys
import typing
import csv
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QLineEdit,QPushButton,QMainWindow,QListWidget,QHBoxLayout,QDialog,QGridLayout,QMessageBox

class Desvincular(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desvincular Empleados")

    #ventanas
        #ventana principal
        ventanaGrande=QVBoxLayout()# integra logo  y subventana
        subVentana=QVBoxLayout()#integra lista a la derecha y ventana derecha
        ventanaderecha=QVBoxLayout()#incluye dos botones derechos
        self.lista=QListWidget()#lista
        self.cargar_empleados()
        self.lista.itemDoubleClicked.connect(self.eliminar_empleado)

        self.titulo = QLabel("Ventana para desvincular empleados")
        self.indicacion = QLabel("Para eliminar un empleado, presione dos veces el empleado a eliminar")
        
        #logo
        logo=QLabel(self)#cambiar al centro
        imagen = QPixmap(r"./logo.png")   
        logo.setPixmap(imagen)
        
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #botones
        volver=QPushButton("volver")
        volver.clicked.connect(lambda:self.close())#creo que se puede achicar la funcion
       

        #asignar widgets
        subVentana.addWidget(self.lista)
        subVentana.addWidget(volver)
        ventanaGrande.addWidget(logo)
        ventanaGrande.addWidget(self.titulo)
        ventanaGrande.addWidget(self.indicacion)
        ventanaGrande.addLayout(subVentana)
        

        #asignar ventanas
        ventana=QWidget()
        subVentana.addLayout(ventanaderecha)
        ventanaGrande.addLayout(subVentana)
        ventana.setLayout(ventanaGrande)
        self.setCentralWidget(ventana)

    def cargar_empleados(self):
        try:
            with open('empleados.csv', newline='') as archivo:
                reader = csv.reader(archivo)
                next(reader)
                for empleado in reader:
                    nombre = empleado[0]
                    self.lista.addItem(nombre)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "El archivo empleados.csv no se encontró.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Ocurrió un error al cargar los empleados: {str(e)}")

    def eliminar_empleado(self, item):
        empleado_seleccionado = item.text()
        respuesta = QMessageBox.question(self, "Confirmación", f"¿Seguro que desea eliminar al empleado '{empleado_seleccionado}'?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if respuesta == QMessageBox.StandardButton.Yes:
            try:
                with open('empleados.csv', 'r') as archivo:
                    empleados = list(csv.reader(archivo))
                with open('empleados.csv', 'w', newline='') as archivo:
                    writer = csv.writer(archivo)
                    for empleado in empleados:
                        if empleado[0] != empleado_seleccionado:
                            writer.writerow(empleado)
                
                self.lista.takeItem(self.lista.row(item))
            except FileNotFoundError:
                QMessageBox.warning(self, "Error", "El archivo empleados.csv no se encontró.")
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Ocurrió un error al eliminar el empleado: {str(e)}")
  

if __name__=="__main__":
    app=QApplication(sys.argv)
    ventana=Desvincular()
    ventana.show()
    sys.exit(app.exec())