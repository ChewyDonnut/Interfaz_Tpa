import csv
from PyQt6.QtWidgets import QWidget, QCalendarWidget, QApplication, QComboBox, QMainWindow, QLabel, QVBoxLayout, QPushButton, QDialog, QMessageBox

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Nombre Empresa")

        self.boton_crear = QPushButton("Crear Turno")
        self.boton_crear.clicked.connect(self.mostrar_ventana_turno)

        self.boton_modificar = QPushButton("Modificar Turno")
        self.boton_modificar.clicked.connect(self.mostrar_ventana_modificar)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Interfaz Principal"))
        layout.addWidget(self.boton_crear)
        layout.addWidget(self.boton_modificar)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mostrar_ventana_turno(self):
        ventana_turno = VentanaRegistro()
        ventana_turno.exec()

    def mostrar_ventana_modificar(self):
        ventana_modificar = VentanaModificar()
        ventana_modificar.exec()

class VentanaRegistro(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Turnos Nombre Empresa")
        self.init_ui()

    def init_ui(self):
        self.calendario = QCalendarWidget()
        self.etiqueta_fecha_hora = QLabel("Turno")
        self.campo_horario = QComboBox()
        self.etiqueta_empleado = QLabel("Empleado")
        self.campo_empleado = QComboBox()

        self.cargar_empleados_csv()

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)

        self.campo_horario.addItem("Mañana")
        self.campo_horario.addItem("Tarde")
        self.campo_horario.addItem("Noche")

        layout = QVBoxLayout()
        layout.addWidget(self.calendario)
        layout.addWidget(self.etiqueta_fecha_hora)
        layout.addWidget(self.campo_horario)
        layout.addWidget(self.etiqueta_empleado)
        layout.addWidget(self.campo_empleado)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def cargar_empleados_csv(self):
        with open("empleados.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  # Saltar la primera fila de encabezado
            for row in reader:
                empleado = row[0]
                with open("empleados.csv", "r") as roles_csv:
                    roles_reader = csv.reader(roles_csv)
                    for roles_row in roles_reader:
                        if empleado == roles_row[0]:
                            rol = roles_row[1]
                            self.campo_empleado.addItem(empleado, userData=rol)  # Usar userData para almacenar el rol
                            break

    def guardar_datos(self):
        dia = self.calendario.selectedDate().toString('yyyy-MM-dd')
        horario = self.campo_horario.currentText()
        empleado = self.campo_empleado.currentText()
        rol = self.campo_empleado.currentData()  # Obtener el rol del empleado seleccionado

        if horario == "Mañana":
            horario = "08:00 a 16:00"
        elif horario == "Tarde":
            horario = "16:00 a 00:00"
        elif horario == "Noche":
            horario = "00:00 a 08:00"
        else:
            horario = ""

        existente = any(
            row[0] == empleado and row[2] == dia
            for row in csv.reader(open("Turnos.csv", "r"))
        )

        if not existente:
            with open("Turnos.csv", "a", newline="") as archivo_csv:
                writer = csv.writer(archivo_csv)
                writer.writerow(["Nombre", "Turno", "Fecha", "Rol"])  # Agregar la primera fila de encabezado

                writer.writerow([empleado, horario, dia, rol])  # Agregar el rol en la fila
            QMessageBox.information(self, "Turnos Nombre Empresa", "Turno creado exitosamente.")
        else:
            QMessageBox.information(self, "Turnos Nombre Empresa", "El turno ya existe para el empleado seleccionado.")

class VentanaModificar(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar Turno")
        self.init_ui()

    def init_ui(self):
        self.campo_empleado = QComboBox()
        self.campo_fecha = QComboBox()
        self.campo_horario = QComboBox()
        self.campo_horario.addItem("Mañana")
        self.campo_horario.addItem("Tarde")
        self.campo_horario.addItem("Noche")
        self.boton_modificar = QPushButton("Modificar")
        self.boton_modificar.clicked.connect(self.modificar_turno)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Modificar Turno"))
        layout.addWidget(QLabel("Empleado:"))
        layout.addWidget(self.campo_empleado)
        layout.addWidget(QLabel("Fecha:"))
        layout.addWidget(self.campo_fecha)
        layout.addWidget(QLabel("Nuevo Horario:"))
        layout.addWidget(self.campo_horario)
        layout.addWidget(self.boton_modificar)

        self.setLayout(layout)
        self.cargar_datos()

    def cargar_datos(self):
        empleados = set()
        fechas = set()
        with open("Turnos.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  # Saltar la primera fila de encabezado
            for row in reader:
                empleados.add(row[0])
                fechas.add(row[2])

        self.campo_empleado.addItems(sorted(empleados))
        self.campo_fecha.addItems(sorted(fechas))

    def modificar_turno(self):
        empleado = self.campo_empleado.currentText()
        fecha = self.campo_fecha.currentText()
        horario = self.campo_horario.currentText()

        if horario == "Mañana":
            nuevo_horario = "08:00 a 16:00"
        elif horario == "Tarde":
            nuevo_horario = "16:00 a 00:00"
        elif horario == "Noche":
            nuevo_horario = "00:00 a 08:00"
        else:
            nuevo_horario = ""

        filas = []
        encontrado = False

        # Leer todas las filas del archivo CSV
        with open("Turnos.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            for fila in reader:
                filas.append(fila)
                if fila[0] == empleado and fila[2] == fecha:
                    fila[1] = nuevo_horario
                    encontrado = True

        # Escribir las filas actualizadas en el archivo CSV
        with open("Turnos.csv", "w", newline="") as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerows(filas)

        if encontrado:
            QMessageBox.information(self, "Modificar Turno", "Turno modificado exitosamente.")
        else:
            QMessageBox.information(self, "Modificar Turno", "No se encontró el turno especificado.")

if __name__ == '__main__':
    app = QApplication([])
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    app.exec()
