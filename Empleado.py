import csv

class Empleado:
    def __init__(self, nombre, rol, usuario, clave, turnos=[], tareas=[]):
        self.nombre = nombre
        self.rol = rol
        self.usuario = usuario
        self.clave = clave
        self.turnos = turnos
        self.tareas = tareas

# Crear una lista vacía para almacenar los empleados
lista_empleados = []

def crear_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    rol = input("Ingrese el rol del empleado: ")
    usuario = input("Ingrese el usuario del empleado: ")
    clave = input("Ingrese la clave del empleado: ")
    
    empleado = Empleado(nombre, rol, usuario, clave)
    
    lista_empleados.append(empleado)
    print("Empleado creado con éxito.")

# Llamar a la función para crear un empleado
crear_empleado()

# Guardar los empleados en un archivo CSV
nombre_archivo = "empleados.csv"

with open(nombre_archivo, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['Nombre', 'Rol', 'Usuario', 'Clave', 'Turnos', 'Tareas'])
    
    for empleado in lista_empleados:
        writer.writerow([empleado.nombre, empleado.rol, empleado.usuario, empleado.clave, empleado.turnos, empleado.tareas])

print("Los empleados se han guardado en el archivo", nombre_archivo)
