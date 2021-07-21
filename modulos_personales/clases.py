# Importacion de modulos
from datetime import datetime

# Creacion de la clase
class Participante:
    # Atrubutos
    correo = ""
    nombre = ""
    nacimiento = ""
    momento = datetime.strftime(datetime.now(),'%d-%m-%Y')

    # Metodo Constructor
    def __init__(self, correo, nombre , nacimiento,
                momento= datetime.strftime(datetime.now(),'%d-%m-%Y %H:%M')):
        self.correo=correo
        self.nombre=nombre
        self.nacimiento=nacimiento
        self.momento=momento