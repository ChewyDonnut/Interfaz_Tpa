import sys
import csv
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QGridLayout,QMessageBox, QVBoxLayout, QDialog, QHBoxLayout, QLineEdit, QTableWidget,QTableWidgetItem
class VentanaHorarios(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horarios Asignados")
        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Empleado", "Horario", "Fecha"])

        self.cargar_horarios()

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def cargar_horarios(self):
        with open("Turnos.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  # Saltar la primera fila de encabezado

            row_count = sum(1 for _ in reader)
            self.table_widget.setRowCount(row_count)

            archivo_csv.seek(0)  # Volver al inicio del archivo
            next(reader)  # Saltar la primera fila de encabezado nuevamente

            row_index = 0
            for row in reader:
                empleado = row[0]
                horario = row[1]
                fecha = row[2]

                item_empleado = QTableWidgetItem(empleado)
                item_horario = QTableWidgetItem(horario)
                item_fecha = QTableWidgetItem(fecha)

                self.table_widget.setItem(row_index, 0, item_empleado)
                self.table_widget.setItem(row_index, 1, item_horario)
                self.table_widget.setItem(row_index, 2, item_fecha)

                row_index += 1


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

        #Conectar botón
        self.boton_confirmar.clicked.connect(self.cambiar_contrasena)

        #Contenedores
        entradas = QGridLayout()
        entradas.addWidget(self.texto_contrasena, 0, 0)
        entradas.addWidget(self.entrada_contrasena, 0, 1)
        entradas.addWidget(self.texto_confirmar, 1, 0)
        entradas.addWidget(self.entrada_confirmar, 1, 1)

        entradas_widget = QWidget()
        entradas_widget.setLayout(entradas)
        
        contenedor = QVBoxLayout()
        contenedor.addWidget(self.texto)
        contenedor.addWidget(entradas_widget)
        contenedor.addWidget(self.boton_confirmar)

        self.setLayout(contenedor)

    def cambiar_contrasena(self):
        nueva_contrasena = self.entrada_contrasena.text()
        confirmar_contrasena = self.entrada_confirmar.text()
        if not nueva_contrasena and not confirmar_contrasena:
            QMessageBox.information(self,"Error","Rellene todos los campos")
        else:
            if nueva_contrasena == confirmar_contrasena:
                nombre_usuario = self.nombre_usuario
        
                # Leer el archivo CSV y actualizar la contraseña
                filas_actualizadas = []
                with open("empleados.csv", "r") as archivo_csv:
                    lector_csv = csv.reader(archivo_csv)
                    encabezados = next(lector_csv)  # Leer los encabezados
                    filas_actualizadas.append(encabezados)  # Agregar los encabezados a las filas actualizadas
                    for fila in lector_csv:
                        if fila[0] == nombre_usuario:
                            fila[3] = nueva_contrasena  # Actualizar la contraseña en la fila correspondiente
                        filas_actualizadas.append(fila)

                # Escribir las filas actualizadas en el archivo CSV
                with open("empleados.csv", "w", newline='') as archivo_csv:
                    escritor_csv = csv.writer(archivo_csv)
                    escritor_csv.writerows(filas_actualizadas)

                # Mostrar mensaje de éxito al usuario
                QMessageBox.information(self, "Cambio de contraseña", "La contraseña se ha cambiado exitosamente.")
            else:
                # Mostrar mensaje de error al usuario
                QMessageBox.warning(self, "Error", "Las contraseñas no coinciden. Por favor, inténtalo nuevamente.")

        # Limpiar las entradas de contraseña
            self.entrada_contrasena.clear()
            self.entrada_confirmar.clear()
            self.close()


class VentanaEmpleado(QWidget):
    def __init__(self, nombre_usuario=None, rol=None):
        super().__init__()
        self.setWindowTitle("Ventana Empleado")
        # ventanas
        self.ver_turnos = VentanaHorarios()
        self.cambiar_con = CambiarContrasena()

        # Elementos
        logo = QLabel(self)
        imagen = QPixmap(r"./logo.png")
        logo.setPixmap(imagen)
        self.bienvenida = QLabel(f"Bienvenido/a: {nombre_usuario}")

        # centrar textos
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton_cambiar = QPushButton("Cambiar contraseña")
        self.boton_ver_turnos = QPushButton("Ver turnos")

        self.lista_pendientes = QLabel()

        # conectar botones
        self.boton_ver_turnos.clicked.connect(lambda: self.desplegar(1))
        self.boton_cambiar.clicked.connect(self.abrir_cambiar_contrasena)

        # Contenedores
        botones = QGridLayout()
        botones.addWidget(self.boton_cambiar, 0, 0)
        botones.addWidget(self.boton_ver_turnos,0,1)

        botones_widget = QWidget()

        botones_widget.setLayout(botones)

        contenedor = QVBoxLayout()
        contenedor.addWidget(logo)
        contenedor.addWidget(self.bienvenida)
        contenedor.addWidget(botones_widget)
        contenedor.addWidget(self.lista_pendientes)

        self.setLayout(contenedor)

        self.nombre_usuario = nombre_usuario

    def abrir_cambiar_contrasena(self):
        self.cambiar_con.nombre_usuario = self.nombre_usuario
        self.cambiar_con.exec()
    def desplegar(self, id: int):
        if id == 1:
            if self.ver_turnos.isHidden():
                self.ver_turnos.show()
            else:
                self.ver_turnos.hide()
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