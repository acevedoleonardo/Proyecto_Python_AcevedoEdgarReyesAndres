#Proyecto_de_Python 
#Integrantes:_Andres_Reyes
#Edgar_Leonardo_Acevedo 
#-----------------------------------------------------------------------------------------------------------------------------
from cordinator_Modulo import *             #Llamada a Modulo al cordinador  principal 
from trainer_Modulo import *                #Llamada a Modulo al trainer 
from campers_Modulo import *                #Llamada a modulo Campers
from notas import *                         #Lllamada a modulo de notas 

print("Bienvenido a Campuslands")
print("\n==== User Login ====")
print("----------------------------------------------")
print("Ingrese la opcion numerica que corresponda... ")
print("----------------------------------------------")
print("1. Cordinator")
print("2. Trainer")
print("3. Camper")
print("4. Salir")
option=input("Seleccione una Opción:")                 #Se crea una variable para almacenar la opcion que ingrese el usuario

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
    print("Opción inválida, por favor intente nuevamente.")




