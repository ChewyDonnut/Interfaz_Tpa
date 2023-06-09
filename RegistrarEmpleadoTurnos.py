from PyQt6.QtWidgets import QWidget, QApplication,QDateTimeEdit, QComboBox, QMainWindow, QLabel, QVBoxLayout, QPushButton, QDialog, QMessageBox, QLineEdit, QHBoxLayout
from PyQt6.QtCore import QDateTime
from Empleado import Empleado
from Turno import Turno
Lista_empleados = []
lista_turnos = []

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Nombre Empresa")

        # self.boton_registrar = QPushButton("Registrar Empleado")
        # self.boton_registrar.clicked.connect(lambda: self.funcion_auxiliar(1))

        self.boton_crear = QPushButton("Crear Turno")
        self.boton_crear.clicked.connect(lambda: self.funcion_auxiliar(2))

        self.boton_modificar = QPushButton("Modificar Turno")
        self.boton_modificar.clicked.connect(lambda: self.funcion_auxiliar(3))

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Interfaz Principal"))
        # layout.addWidget(self.boton_registrar)
        layout.addWidget(self.boton_crear)
        layout.addWidget(self.boton_modificar)

        central_widget = QDialog()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def funcion_auxiliar(self,id):
        # if id == 1:
        #     ventana_registro = VentanaRegistro()
        #     ventana_registro.exec()
        if id == 2:
            ventana_turno = VentanaTurnos()
            ventana_turno.exec()
        elif id == 3:
            ventana_modificar = VentanaModificar()
            ventana_modificar.exec()


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
        self.etiqueta_contrasena = QLabel("Contrasena:")
        self.campo_contrasena = QLineEdit()

        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.clicked.connect(self.guardar_datos)

        layout = QVBoxLayout()
        layout.addWidget(self.etiqueta_nombre)
        layout.addWidget(self.campo_nombre)
        layout.addWidget(self.etiqueta_rol)
        layout.addWidget(self.campo_rol)
        layout.addWidget(self.etiqueta_usuario)
        layout.addWidget(self.campo_usuario)
        layout.addWidget(self.etiqueta_contrasena)
        layout.addWidget(self.campo_contrasena)
        layout.addWidget(self.boton_guardar)

        self.setLayout(layout)

    def guardar_datos(self):                    # funcion de guardar datos 
        nombre = self.campo_nombre.text()
        rol = self.campo_rol.text()
        usuario = self.campo_usuario.text()
        contrasena = self.campo_contrasena.text()
        a=nombre.replace(" ","")
        b=usuario.replace(" ","")
        c=contrasena.replace(" ","")
        d=rol.replace(" ","")
        if a=="" or b=="" or c=="" or c=="":
           print("vacioooo")
        else:
            Lista_empleados.append(Empleado(nombre,rol,usuario,contrasena))
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
        for i in range(len(Lista_empleados)):
            self.campo_empleado.addItem(Lista_empleados[i].getNombre())

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
        empleado = self.campo_empleado.currentText()
        lista_turnos.append(Turno(empleado,fecha))

        QMessageBox.information(self, "Turnos nombre empresa", "Turno creado exitosamente.")
        self.close()

class VentanaModificar(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modificar turnos")
        #Elementos
        texto = QLabel("Modificar turno")
        etiqueta_turno = QLabel("Turno")
        self.turnos = QComboBox()
        self.boton_aceptar = QPushButton("Aceptar")
        #Config
        self.turnos.addItems(lista_turnos)
        self.boton_aceptar.clicked.connect(lambda: self.desplegar(1))

        #Contenedores
        campos = QHBoxLayout()
        campos.addWidget(etiqueta_turno)
        campos.addWidget(self.turnos)
        
        campos_widget = QWidget()
        campos_widget.setLayout(campos)

        contenedor = QVBoxLayout()
        contenedor.addWidget(texto)
        contenedor.addWidget(campos_widget)
        contenedor.addWidget(self.boton_aceptar)

        self.setLayout(contenedor)
    
    def desplegar(self,id):
        if id == 1:
            ventana_modificando = VentanaModificando()
            ventana_modificando.exec()

class VentanaModificando(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Modificando turno")

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
