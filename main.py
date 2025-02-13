<<<<<<< HEAD
=======
import json                                 #Se importa las bases de datos 
>>>>>>> 0e4af4b (Programa funcional)
#Proyecto_de_Python 
#Integrantes:_Andres_Reyes
#Edgar_Leonardo_Acevedo 
#-----------------------------------------------------------------------------------------------------------------------------
<<<<<<< HEAD
=======

>>>>>>> 0e4af4b (Programa funcional)
from cordinator_Modulo import *             #Llamada a Modulo al cordinador  principal 
from trainer_Modulo import *                #Llamada a Modulo al trainer 
from campers_Modulo import *                #Llamada a modulo Campers
from notas import *                         #Lllamada a modulo de notas 
<<<<<<< HEAD

print("Bienvenido a Campuslands")
print("\n==== User Login ====")
print("----------------------------------------------")
print("Ingrese la opcion numerica que corresponda... ")
print("----------------------------------------------")
=======
print("----------------------------------------------")
print("Bienvenido a Campuslands")
print("\n==== User Login ====")
print("----------------------------------------------")
print("Seleccione la opcion dependiendo de su Rol")
>>>>>>> 0e4af4b (Programa funcional)
print("1. Cordinator")
print("2. Trainer")
print("3. Camper")
print("4. Salir")
option=input("Seleccione una Opción:")                 #Se crea una variable para almacenar la opcion que ingrese el usuario

<<<<<<< HEAD
if option == "1":                                       #La condicional if es para dictaminar que decision tomo el usuario. 
    print("Eres el Cordinador")
    login_cordinator()
elif option == "2":
    print("Eres el Trainer ")
    Registrar_Trainer()
elif option == "3": 
    print("Eres un camper")
    Registrarcamper()
elif option == "4": 
    print("Hasta pronto...!")                                  
else: 
=======
if option == "1":
    print("-------------------------------------------------")
    print("==Bienvenido Coordinador==")
    print("-------------------------------------------------")
    login_cordinator()
    menu_camper()
elif option == "2":    
    print("-------------------------------------------------")
    print("==Bienvenido Trainer==")
    print("-------------------------------------------------")
    print("Temporalmente La Opcion no se encuentra disponible,  Lamentamos las molestias causadas!!!")
elif option == "3":
    print("-------------------------------------------------")
    print("==Bienvenido Campers==")
    print("-------------------------------------------------")
    menu_campers()
elif option == "4":
    print("Hasta pronto...!")
    exit()
else:
>>>>>>> 0e4af4b (Programa funcional)
    print("Opción inválida, por favor intente nuevamente.")




