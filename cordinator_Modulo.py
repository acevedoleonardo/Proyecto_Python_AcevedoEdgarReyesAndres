import json

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

