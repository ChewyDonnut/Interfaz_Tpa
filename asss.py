import csv
with open("Turnos.csv", "r") as archivo_csv:
            reader = csv.reader(archivo_csv)
            for row in reader:
                print(row[1])