import json
from campers_Modulo import *                #Llamada a modulo Campers
from notas_Campers import *                   #Lllamada a modulo de notas

def abrirJSON():
    dicFinal = {}                                               #Se crea un diccionario 
    with open('./cordinator_Bdd.json', 'r') as openFile:             #Se abre la base de datos 
        dicFinal = json.load(openFile)
    print("Se abrió el archivo")
    return dicFinal

def guardarJSON(dic):
    with open('./cordinator_Bdd.json', 'w') as outFile:
        json.dump(dic, outFile, indent=4)                       # indent=4 para una mejor visualización
    print("Se guardó el archivo exitosamente")
    return True

#Creamos una funcion para implementar el menu

def login_cordinator():     
        print("---------------------------------------------------------------------------")
        print("=== Bienvenido Cordinador ===")
        print("---------------------------------------------------------------------------")
        usuario=input("Ingrese su Usurio: ")
        contrasena=input("Ingrese su password: ")
            
def menu():
        print("--------------------------------------------------------------------------")
        print("\n--- Menú Principal ---")
        print("1. Mostrar Campers registrados")
        print("2. Registrar Notas (Coordinador)")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            main()
            
        elif opcion=="2":
            RegistrarNotas()
            
        elif opcion == "3":
            print("Saliendo del programa...")
            exit() 


