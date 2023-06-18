import sys
import csv
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QTableView, QHBoxLayout, QDialog, QGridLayout, QMessageBox

class EmployeeTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.data)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.data[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            return str(self.data[row][col])

        return None

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return f"Columna {section + 1}"
            elif orientation == Qt.Orientation.Vertical:
                return f"Fila {section + 1}"

        return None

class Desvincular(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar Contraseña")

        #ventanas
        #ventana principal
        ventanaGrande=QVBoxLayout()# integra logo  y subventana
        subVentana=QHBoxLayout()#integra lista a la derecha y ventana derecha
        ventanaderecha=QVBoxLayout()#incluye dos botones derechos
        self.lista=QTableView()#lista
      
        
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
        self.titulo=QLabel("Desvinculación de usuario")#aqui va el nombre de la persona tambien 
        self.usuario=QLabel("Usuario")
        #dato a ingresar
        self.eliminar_usuario=QLineEdit("")#nombre de usuario
        #boton
        cambiar=QPushButton("Desvincular")
        cambiar.clicked.connect(self.confirmacion)
        #asignar los al grid
        datos.addWidget(self.usuario, 0, 0)
        datos.addWidget(self.eliminar_usuario, 0, 1)

        self.vista_tabla = QTableView()
        ventanita.addWidget(self.titulo)
        ventanita.addLayout(datos)
        ventanita.addWidget(cambiar)
        ventanita.addWidget(self.vista_tabla)
        self.setLayout(ventanita)

        self.load_employee_data()

    def load_employee_data(self):
        file_path = "empleados.csv"
        employee_data = self.read_csv(file_path)
        if employee_data:
            model = EmployeeTableModel(employee_data)
            self.vista_tabla.setModel(model)

    def read_csv(self, file_path):
        employee_data = []
        try:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    employee_data.append(row)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Archivo no encontrado: empleados.csv")
        return employee_data

    def write_csv(self, file_path, data):
        try:
            with open(file_path, "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Archivo no encontrado: empleados.csv")

    def confirmacion(self):
        user_name = self.eliminar_usuario.text().strip()
        if user_name:
            file_path = "empleados.csv"
            employee_data = self.read_csv(file_path)
            if employee_data:
                updated_employee_data = [employee for employee in employee_data if employee[0] != user_name]
                if len(updated_employee_data) < len(employee_data):
                    reply = QMessageBox.question(self, "Confirmar Desvinculación", "¿Estás seguro que deseas desvincular al empleado?",
                                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
                    if reply == QMessageBox.StandardButton.Yes:
                        self.write_csv(file_path, updated_employee_data)
                        self.load_employee_data()
                else:
                    QMessageBox.information(self, "Empleados (Nombre Empresa)", "El usuario no fue encontrado.")
        else:
            QMessageBox.information(self, "Empleados (Nombre Empresa)", "Por favor ingresa un usuario.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Desvincular()
    ventana.show()
    sys.exit(app.exec())