class Turno:
    def __init__(self,empleado,fecha):
        self.empleado = empleado
        self.fecha = fecha
    
    def __str__(self):
        return f"{self.fecha}"

    def getEmpleadoTurno(self):
        return self.empleado
    def getFecha(self):
        return self.fecha