class Empleado:
    def __init__(self, nombre, rol, usuario, clave, turnos=[], tareas = []):
        self.nombre = nombre
        self.rol = rol 
        self.usuario = usuario
        self.clave = clave
        self.turnos = turnos
        self.tareas = tareas
        
    def __str__(self) -> str:
        return f'''
            Nombre Empleado: {self.nombre} 
            Rol:  {self.rol} 
            Usuario: {self.usuario}
            Contraseña: {self.clave}
            '''
    def getContrasena(self):
        return self.clave
    def getUsuario(self):
        return self.usuario
    def getRol(self):
        return self.rol
    def getNombre(self):
        return self.nombre
    def getTurnos(self):
        return self.turnos
    def getTareas(self):
        return self.tareas
    def modContrasena(self,nueva):
        self.clave = nueva