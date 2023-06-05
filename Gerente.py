from Empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, rol, usuario, clave, turnos=[], tareas=[]):
        super().__init__(nombre, rol, usuario, clave, turnos, tareas)
