# Area de importacion.
# from funciones import participantes
from modulos_personales.clases import Participante
from modulos_personales import regEx
from collections import OrderedDict
from funciones import *
import os
import re
import json

# Funciones Necesarias.
"""
Funciones que no puden estar en otro archivo, ya que luego hay errores 
en la busqueda de objetos en la lista.
"""
def BuscarCorreo(correoBuscar):
    coincidencia=False
    for partcipante in participantes:
        if (partcipante.correo==correoBuscar):
            coincidencia=True
            break
    return coincidencia

def BuscarEmail(correoBuscar):
    contador=-1
    indice_retorno=-1
    for partipante in participantes:
        contador+=1
        if (partipante.correo==correoBuscar):
            indice_retorno=contador
            break
    return indice_retorno

# Creacion de variables
ruta = os.path.abspath(os.getcwd())
archivo_normal=ruta+"\\participantes.csv"
archivo_respaldo=ruta+"\\participantes.bak"
participantes = list(OrderedDict.fromkeys(participantes))

# Funcionalidad del Programa.
def main(Participante):
    while True:
        # Menu de opciones.
        print("\n----------------Menu----------------\n")
        print("[1] Cargar informacion de CSV.")
        print("[2] Registrar Participantes.")
        print("[3] Buscar Participante.")
        print("[4] Modificar Participante.")
        print("[5] Eliminar Participante.")
        print("[6] Ver lista de participantes.")
        print("[7] Actuializar Informacion de CSV.")
        print("[8] Serializar Informacion a JSON.")
        print("[X] Salir del programa.\n")

        opcion_menu = input("¿Que opcion deseas? ").lower()

        # Funcion del programa
        # Cargar informacion de CSV.
        if opcion_menu == '1':
            cargarDatos()
        # Registrar Participantes.
        elif opcion_menu == '2':
            # Registro de datos
            while True:
                print("Ingresa el correo electronico")
                correo = input("(Deja el espacio vacio para volver al menu principal) ")
                # Valida el correo
                if(re.search(regEx.regexCorreo,correo)):
                    # Verifica si el correa esta o no en la lista.
                    coincidencia = BuscarCorreo(correo)
                    if(coincidencia == True):
                        # Si esta rompe ciclo y devuelve al menu de opciones.
                        print("\nEse correo ya esta registrado...")
                        print("Volviendo al menu principal...\n")
                        break
                    else:
                        # Si no lo esta, elprograma pide el resto de datos.
                        nombre = str(input("Ingresa el Nombre: "))
                        while True:
                            # Valida que ingrese una fecha valida
                            fnac = str(input("Ingresa la Fecha de Nacimiento (Formato ##-##-####): "))
                            if(re.search(regEx.regexFecha,fnac)):
                                # Rompe el ciclo cuanodo ya se haya ingresado bien.
                                # Finaliza Guardando los datos en una lista de objetos.
                                print("\nGuardando los datos...")
                                participantes.append(Participante(correo, nombre, fnac))
                                print("Datos Guardados.\n ")
                                break
                            else:
                                # Informa que no se ingreso correctamente.
                                print("\nIngrese una fecha con el formato que se indica..\n")
                # Si no pone un correo
                elif correo == "":
                    #Se devuelve al menu principal.
                    break
                else:
                    print("\nVerifique que haya ingresado un correo electronico.\n")
        # Buscar Participante.
        elif opcion_menu == '3':
            while True:
                print("Ingresa el correo electronico")
                correo = input("(Deja el espacio vacio para volver al menu principal) ")
                # Valida el correo
                if (re.search(regEx.regexCorreo, correo)):
                    # Verifica si el correa esta o no en la lista.
                    indice_obtenido = BuscarEmail(correo)
                    if (indice_obtenido == -1):
                        # Si no existe deja un mensaje para volver al menu
                        print("Participante no registrado.")
                        print("Favor de registrar al Participante.")
                        input("Presione enter para continuar.")
                        break
                    else:
                        # Si existe muetsra la informacion
                        print("\n------------Informacion del Participante------------\n")
                        print("Correo:      ",participantes[indice_obtenido].correo)
                        print("Nombre:      ",participantes[indice_obtenido].nombre)
                        print("Nacimiento:  ",participantes[indice_obtenido].nacimiento)
                        print("Registro:    ",participantes[indice_obtenido].momento,"\n")
                        # Pregunta si quiere buscar otro usuario
                        resp = input("Presione enter para volver al menu."
                                    "\nDe lo contario ingrese cualquier letra: ").upper()
                        if resp == '':
                            break
                elif correo == "":
                    #Se devuelve al menu principal.
                    break
                else:
                    print("\nVerifique que haya ingresado un correo electronico.\n")
        # Modificar Participante.
        elif opcion_menu == '4':
            while True:
                print("Ingresa el correo electronico")
                correo = input("(Deja el espacio vacio para volver al menu principal) ")

                if (re.search(regEx.regexCorreo, correo)):
                    # Verifica si el correa esta o no en la lista.
                    indice_obtenido = BuscarEmail(correo)
                    if (indice_obtenido == -1):
                        # Si no existe deja un mensaje para volver al menu
                        print("Participante no registrado.")
                        print("Favor de registrar al Participante.")
                        input("Presione enter para continuar.")
                        break
                    else:
                        # Si existe muetsra la informacion
                        print("\n------------Informacion del Participante------------\n")
                        print("Correo:      ", participantes[indice_obtenido].correo)
                        print("Nombre:      ", participantes[indice_obtenido].nombre)
                        print("Nacimiento:  ", participantes[indice_obtenido].nacimiento)
                        print("Registro:    ", participantes[indice_obtenido].momento, "\n")
                        # Elimino la el objeto de la lista para reemplazarla con el nuevo objeto.
                        participantes.pop(indice_obtenido)
                        nombre = str(input("Ingresa el Nombre: "))
                        while True:
                            # Valida que ingrese una fecha valida
                            fnac = str(input("Ingresa la Fecha de Nacimiento (Formato ##-##-####): "))
                            if (re.search(regEx.regexFecha, fnac)):
                                # Rompe el ciclo cuanodo ya se haya ingresado bien.
                                # Finaliza Guardando los datos en una lista de objetos.
                                print("\nGuardando los datos...")
                                participantes.append(Participante(correo, nombre, fnac))
                                print("Datos Guardados.\n ")
                                break
                        break
                elif correo == "":
                    #Se devuelve al menu principal.
                    break
                else:
                    print("\nVerifique que haya ingresado un correo electronico.\n")
        # Eliminar Participante.
        elif opcion_menu == '5':
            while True:
                print("Ingresa el correo electronico")
                correo = input("(Deja el espacio vacio para volver al menu principal) ")

                if (re.search(regEx.regexCorreo, correo)):
                    # Verifica si el correa esta o no en la lista.
                    indice_obtenido = BuscarEmail(correo)
                    if (indice_obtenido == -1):
                        # Si no existe deja un mensaje para volver al menu
                        print("Participante no registrado.")
                        print("Favor de registrar al Participante.")
                        input("Presione enter para continuar.\n")
                        break
                    else:
                        # Si existe muetsra la informacion
                        print("\n------------Informacion del Participante------------\n")
                        print("Correo:      ", participantes[indice_obtenido].correo)
                        print("Nombre:      ", participantes[indice_obtenido].nombre)
                        print("Nacimiento:  ", participantes[indice_obtenido].nacimiento)
                        print("Registro:    ", participantes[indice_obtenido].momento, "\n")
                        resp_supr = input("¿Esta seguro de eliminar este registro? [Y/N] ").upper()
                        if resp_supr == 'Y':
                            print("\nEliminando registros del participante...")
                            participantes.pop(indice_obtenido)
                            print("Registro eliminado.")
                            input("Presione enter para continuar.\n")
                            break
                        else:
                            print("\nRegresando al menu....")
                            input("Presione enter para continuar\n")
                elif correo == "":
                    #Se devuelve al menu principal.
                    break
                else:
                    print("\nVerifique que haya ingresado un correo electronico.\n")
        # Ver lista de Participantes.
        elif opcion_menu == '6':
            # Tabular
            print("{:>20} {:>20} {:>20} {:>20}".format(
                "CORREO",
                "NOMBRE",
                "NACIMIENTO",
                "REGISTRO"))
            print("{:>20} {:>20} {:>20} {:>20}".format(
                "-----------------",
                "-----------------",
                "-----------------",
                "-----------------"))
            element = 2
            for element in participantes:
                print("{:>20} {:>20} {:>20} {:>20}".format(element.correo,element.nombre,
                                                    element.nacimiento,element.momento))
            input("\nPresione enter para continuar\n")
        # Actualizar CSV.
        elif opcion_menu == '7':
            # Si el archivo existe.
            if os.path.exists('participantes.csv'):
                # Verifico si hay un reespaldo
                if os.path.exists(archivo_respaldo):
                    # Elimino el reespaldo y creo uno nuevo apartir del csv
                    os.remove(archivo_respaldo)
                    os.rename(archivo_normal,archivo_respaldo)
                    print("\nRespaldo Realizado con exito.\n")
                else:
                    os.rename(archivo_normal, archivo_respaldo)
                    print("\nRespaldo Realizado con exito.\n")
            # Si el archivo existe, lo elimino y lo reemplazo con la nueva informacion.
            if os.path.exists('participantes.csv'):
                os.remove('participantes.csv')

            f = open('participantes.csv',"w+")

            # Escribo los encabezados de mi CSV
            f.write("CORREO|NOMBRE|NACIMIENTO|MOMENTO\n")

            # Cierro y abro el archivo para escribir en una linea diferente
            f.close()
            f = open(archivo_normal, "a")

            for Participante in participantes:
                f.write(f'{Participante.correo}|{Participante.nombre}'
                        f'|{Participante.nacimiento}|{Participante.momento}\n')
            f.close()
            print("\nArchivo Actualizado Con Exito.\n")
        # Serializar a JSON
        elif opcion_menu == '8':
            # Serializamos la lista de objetos a json
            json_data = json.dumps(participantes, default=lambda o: o.__dict__, indent=4)
            # Mostramos las lista serializada.
            print(json_data)
            input("Presiona enter para continuar ")
        # Salir del programa.
        elif opcion_menu == 'x':
            #Finaliza el programa
            print("\nFinalizando Programa...")
            print("Vuelva pronto :D...")
            exit()

main(Participante)
