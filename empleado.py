class Empleado:
    
    def __init__(self, nombre, rol, usuario, contraseña):
        self.nombre = nombre
        self.rol = rol 
        self.usuario = usuario
        self.contraseña = contraseña
        
    def __str__(self) -> str:
        return f'''
            Nombre Empleado: {self.nombre} 
            Rol:  {self.rol} 
            Usuario: {self.usuario}
            Contraseña: {self.contraseña}
            '''