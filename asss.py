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


def cargar_empleados_csv(self):
        with open("empleados.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  # Saltar la primera fila de encabezado
            for row in reader:
                empleado = row[0]
                with open("empleados.csv", "r") as claves_csv:
                    clave_reader = csv.reader(claves_csv)
                    for nombre_row in clave_reader:
                        if empleado == nombre_row[0]:
                            clave = nombre_row[3]
                            self.campo_empleado.addItem(empleado, userData=rol)  # Usar userData para almacenar el rol
                            break