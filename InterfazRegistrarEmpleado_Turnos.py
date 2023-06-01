from PyQt6.QtWidgets import QApplication,QDateTimeEdit, QComboBox, QMainWindow, QLabel, QVBoxLayout, QPushButton, QDialog, QMessageBox, QLineEdit
from PyQt6.QtCore import QDateTime
from empleado import Empleado

Lista_empleados = ["Prueba","prueba2"]

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Nombre Empresa")

        self.boton_registrar = QPushButton("Registrar Empleado")
        self.boton_registrar.clicked.connect(self.abrir_ventana_registro)

        self.boton_otra_funcion = QPushButton("Crear Turno")
        self.boton_otra_funcion.clicked.connect(self.otra_funcion)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Interfaz Principal"))
        layout.addWidget(self.boton_registrar)
        layout.addWidget(self.boton_otra_funcion)

        central_widget = QDialog()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def abrir_ventana_registro(self):
        ventana_registro = VentanaRegistro()
        ventana_registro.exec()

    def otra_funcion(self):
        ventana_turno = VentanaTurnos()
        ventana_turno.exec()

class VentanaRegistro(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Registro De Empleados (Nombre Empresa)")

        self.etiqueta_nombre = QLabel("Nombre:")
        self.campo_nombre = QLineEdit()
        self.etiqueta_rol = QLabel("Rol:")
        self.campo_rol = QLineEdit()
        self.etiqueta_usuario = QLabel("Usuario")
        self.campo_usuario = QLineEdit()
        self.etiqueta_contraseña = QLabel("Contraseña:")
        self.campo_contraseña = QLineEdit()

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)

        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(self.etiqueta_rol)
        layout.addWidget(self.campo_rol)
        layout.addWidget(self.etiqueta_usuario)
        layout.addWidget(self.campo_usuario)
        layout.addWidget(self.etiqueta_contraseña)
        layout.addWidget(self.campo_contraseña)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def guardar_datos(self):
        nombre = self.campo_nombre.text()
        rol = self.campo_rol.text()
        usuario = self.campo_usuario.text()
        contraseña = self.campo_contraseña.text()

        a = Empleado(nombre, rol, usuario, contraseña)
        Lista_empleados.append(a)

        print("Lista De Empleados")
        for Info_empleado in Lista_empleados:
            print(Info_empleado)

        QMessageBox.information(self, "Empleados (Nombre Empresa)", "Empleado registrado exitosamente.")
        self.close()


class VentanaTurnos(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Turnos Nombre Empresa")

        self.etiqueta_fecha_hora = QLabel("Fecha")
        self.campo_fecha_hora = QDateTimeEdit()
        self.etiqueta_empleado = QLabel("Empleado")
        self.campo_empleado = QComboBox()
        
        
        #Config
        #Despliega calendario
        self.campo_fecha_hora.setCalendarPopup(True)
        #Solo se pueden ingresar turnos nuevos de la fecha actual en adelante
        self.campo_fecha_hora.setMinimumDateTime(QDateTime.currentDateTime())
        self.campo_empleado.addItems(Lista_empleados)

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)

        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_fecha_hora)
        layout.addWidget(self.campo_fecha_hora)
        layout.addWidget(self.etiqueta_empleado)
        layout.addWidget(self.campo_empleado)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def guardar_datos(self):
        fecha = self.campo_fecha_hora.text()
        print(fecha)


        QMessageBox.information(self, "Turnos nombre empresa", "Turno creado exitosamente.")
        self.close()

if __name__ == '__main__':
    app = QApplication([])
    ventana_principal = VentanaPrincipal()
    ventana_principal.show()
    app.exec()
