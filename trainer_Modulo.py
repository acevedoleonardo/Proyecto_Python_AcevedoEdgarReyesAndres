#Creacion del Menu principal de Trainer

import json

def abrirJSON():
    dicFinal = {}                                               #Se crea un diccionario 
    with open('./trainer_Bdd.json', 'r') as openFile:             #Se abre la base de datos 
        dicFinal = json.load(openFile)
    print("Se abrió el archivo")
    return dicFinal

def guardarJSON(dic):
    with open('./trainer_Bdd.json', 'w') as outFile:
        json.dump(dic, outFile, indent=4)                       # indent=4 para una mejor visualización
    print("Se guardó el archivo exitosamente")
    return True


def Registrar_Trainer():
    print("Registro del Trainer... ")


Registrar_Trainer()

