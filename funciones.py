from modulos_personales.clases import Participante
import os
import csv

ruta = os.path.abspath(os.getcwd())
archivo_normal=ruta+"\\participantes.csv"
archivo_respaldo=ruta+"\\participantes.bak"
participantes = []

def cargarDatos():
    # Verifica si hay algun archivo de datos.
    if os.path.exists(archivo_normal):
        print("")
        # Abro el archivo con delimitadores
        with open('participantes.csv', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv,delimiter='|')
            # Ingreso todos los datos que haya en una lista.
            for e in lector_csv:
                # Eliminamos la fila de los encabezados
                # Revisa si en la fila hay un encabezado
                if "CORREO" in e:
                    # Y utilizamos continue para que no se agregue a la lista.
                    continue
                participantes.append(Participante(e[0],e[1],e[2],e[3]))
    else:
        # Genera el archivo csv.
        f = open(archivo_normal, "w+")

        # Escribe un encabezado.
        f.write("CORREO|NOMBRE|NACIMIENTO|MOMENTO")

        # Cirro el archivo.
        f.close()

cargarDatos()