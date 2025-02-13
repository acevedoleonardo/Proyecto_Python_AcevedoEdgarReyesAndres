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
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#Creamos una funcion para implementar el menu
def login_trainer():
        print("--------------------------------------------------------------------------------------")
        print("=== Bienvenido Trainer ===")
        print("--------------------------------------------------------------------------------------")
        usuario=input("Ingrese su Usurio: ")
        contrasena=input("Ingrese su password: ")    
def menu():
    print("--------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    print("\n--- Menú Principal ---")
    print("1. Mostrar Campers registrados")
    print("2. Registrar Notas (Trainer)")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("En Mantenimiento...!, Disculpe las molestias causadas") 
    elif opcion == "2":
        print("En Mantenimiento...!, Disculpe las molestias causadas")
    elif opcion == "3":
        print("Saliendo del programa...")
        exit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

