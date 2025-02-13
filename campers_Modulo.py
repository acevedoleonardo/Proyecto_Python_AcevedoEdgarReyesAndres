import json                                                          #Se importa las bases de datos

def abrirJSON():
    dicFinal = {}                                                   #Se crea un diccionario 
    with open('./campers_Bdd.json', 'r') as openFile:               #Se abre la base de datos 
        dicFinal = json.load(openFile)                              #Se carga el archivo
    return dicFinal                                                 #Se retorna el diccionario

def guardarJSON(dic):                                               #Funcion para guardar
    with open('./campers_Bdd.json', 'w') as outFile:                #Se abre el archivo
        json.dump(dic, outFile, indent=4)                           #indent=4 para una mejor visualización   
    return True                                                     #Se retorna verdadero

def ordenar():                                                      #Funcion para ordenar
    data = abrirJSON()                                              #Se abre la base de datos 
    campers = data['campers']                                       #Se crea una lista de campers
    return campers                                                  #Se retorna la lista de campers 

campers_list = ordenar()                                           #Se crea una lista de campers
def main():                                                        #Funcion principal 
    campers_list = ordenar()                                       #Se ordena la lista de campers
    for camper in campers_list:                                    #Se recorre la lista de campers                                    
        print("")
        print(camper)                                              #Se imprime la lista de campers

def Registrarcamper():                                             #Funcion para registrar un nuevo campers
    print("--------------------------------------------------------------------------------------")
    print("\n ===Registro de Campers===")
    print("--------------------------------------------------------------------------------------")
    id = input("ID del Camper: ")                               #Se pide el ID del camper       
    Nombre = input("Ingrese el Nombre: ")                      #Se pide el nombre del camper
    Apellido = input("Ingrese el Apellido: ")                                   
    Direccion = input("Ingrese la Dirección: ")
    Telefonos = input("Ingrese el Teléfono: ")
    Estado= input("Ingrese el Estado: ")
    Riesgo= input("Ingrese el Riesgo ")        
    campers_list.append({"id": id, "Nombre": Nombre, "Apellido": Apellido, "Direccion": Direccion, "Telefonos": Telefonos, "Estado": Estado, "Riesgo": Riesgo})       #Se agrega el nuevo camper a la lista de campers
    guardarJSON({"campers": campers_list})                              #Se guarda el nuevo camper en la base de datos
    print("Registro Exitoso")
    print("--------------------------------------------------------------------------------------")

#Menu para el campers 
def menu_campers(): 
    print("-------------------------------------------")
    print("Bienvenido Camper")
    print("1.Desea Registrarse ")
    print("2.Desea ver Listado de Campers registrados ")
    print("3.Desea ver sus notas ")
    print("4.Salir")
    opt=input(":")

    if (opt=="1"):
        Registrarcamper()
    elif (opt=="2"):
        main()
    elif (opt=="3"):
        print("En Mantenimiento...!, Disculpe las molestias causadas")
    elif (opt=="4"):
        print("Hasta pronto...!")
        exit()
    else:   
        print("Opción inválida, por favor intente nuevamente.")

