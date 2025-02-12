import json

def abrirJSON():
    dicFinal = {}                                               #Se crea un diccionario 
    with open('./campers_Bdd.json', 'r') as openFile:             #Se abre la base de datos 
        dicFinal = json.load(openFile)
    print("Se abrió el archivo")
    return dicFinal

def guardarJSON(dic):
    with open('./campers_Bdd.json', 'w') as outFile:
        json.dump(dic, outFile, indent=4)                       # indent=4 para una mejor visualización
    print("Se guardó el archivo exitosamente")
    return True

def ordenar():                                                  #Funcion para ordenar
    data = abrirJSON()
    campers = data['campers']
    return campers

campers_list = ordenar()
for camper in campers_list:
    print(camper)

#Funcion para registrar un nuevo campers
def Registrarcamper():
    print("--------------------------------------------------------------------------------------")
    print("\n ===Agregar Camper===")
    print("--------------------------------------------------------------------------------------")
    id = input("ID del Camper: ")
    Nombre = input("Ingrese el Nombre: ")
    Apellido = input("Ingrese el Apellido: ")
    Direccion = input("Ingrese la Dirección: ")
    Telefonos = input("Ingrese el Teléfono: ")
    Estado = input("Ingrese su estado: (Inscrito, Expulsado, Graduado, Cursando): ")
    Riesgo = input("Ingrese el riesgo: (Bajo, Alto, Medio): ")


    
    #Recorrido para comprar si el camper ya esta registrado
    for camper in campers_list:
        if camper["id"]==id:
            return "El Camper ya esta Registrado!!! "
        
    

    
    # Si el id no existe, agregamos el nuevo camper a la lista
    nuevo_camper = {
        "id": id,
        "nombre": Nombre,
        "apellido": Apellido,
        "direccion": Direccion,
        "telefonos": Telefonos,
        "estado": Estado,
        "riesgo": Riesgo
    }

    #Agregar un nuevo campers a la lista de campers
    campers_list.append(nuevo_camper)
    
    data=abrirJSON()
    data["campers"]=campers_list
    guardarJSON(data)
    return "Camper Registrado Exitosamente..."

Registrarcamper()

