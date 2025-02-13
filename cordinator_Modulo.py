import json
<<<<<<< HEAD
=======
from tkinter import Menu
from campers_Modulo import *                #Llamada a modulo Campers
from notas import *                         #Lllamada a modulo de notas
>>>>>>> 0e4af4b (Programa funcional)

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

<<<<<<< HEAD
def login_cordinator(): 
    print("=== Bienvenido Cordinador ===")
    usuario=input("Ingrese su Usurio: ")
    contraseña=input("Ingrese su password")
login_cordinator()

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Mostrar Campers")
        print("2. Registrar Notas (Coordinador)")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_campers()
        elif opcion == "2":
            camper_id = int(input("Ingrese el ID del camper: "))
            nota_teorica = float(input("Ingrese la nota teórica: "))
            nota_practica = float(input("Ingrese la nota práctica: "))
            registrar_notas(camper_id, nota_teorica, nota_practica)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


menu()

=======
def login_cordinator():     
        usuario=input("Ingrese su Usurio: ")
        contrasena=input("Ingrese su password: ")
            
def menu_camper():
        print("--------------------------------------------------------------------------")
        print("\n---Menu de Asignacion para Campers---")
        print("1. Registrar")
        print("2. Mostrar")
        print("3. Actualizar")
        print("4. ELiminar")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            Registrarcamper()
        elif opcion == "2":
            ordenar()
        elif opcion == "3":
            print("Saliendo del programa...")
            exit() 


>>>>>>> 0e4af4b (Programa funcional)
