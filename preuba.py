from PyQt6.QtWidgets import QApplication, QCalendarWidget

app = QApplication([])
calendario = QCalendarWidget()
fecha_actual = calendario.currentDate()

print(fecha_actual)
