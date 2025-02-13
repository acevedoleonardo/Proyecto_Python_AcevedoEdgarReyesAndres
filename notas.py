<<<<<<< HEAD
def init(self, nombre):
        self.nombre = nombre
        self.nota_teorica = None
        self.nota_practica = None
        self.estado = "Pendiente"

 
def calcular_promedio(self):
        if self.nota_teorica .nota_practica:
            return (self.nota_teorica + self.nota_practica) / 2
        return 


def registrar_nota(self, nombre, nota_teorica, nota_practica):
        for camper in self.campers:
            if camper.nombre == nombre:
                camper.nota_teorica = nota_teorica
                camper.nota_practica = nota_practica
                promedio = camper.calcular_promedio()
                if  promedio >= 60:
                    camper.estado = "Aprobado"
                return f"Notas registradas para {nombre}. Estado: {camper.estado}"
        return "Camper no encontrado."

def mostrar_campers(self):
        for camper in self.campers:
            print(f"Nombre: {camper.nombre}, Estado: {camper.estado}, Promedio: {camper.calcular_promedio()}")

=======
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


def RegistrarNotas():
    campers_list = ordenar()  # Obtener la lista de campers
    id= int(input("Ingrese el id del camper: "))  # Solicitar el ID del camper

    # Buscar el camper por su ID
    camper_encontrado = None
    for camper in campers_list:
        if camper["id"] == id:
            camper_encontrado = camper

    if not camper_encontrado:
        print("Camper no encontrado.")
        return

    # Solicitar las notas teórica y práctica
    notateorica = float(input("Ingrese la nota teórica: "))
    notapractica = float(input("Ingrese la nota práctica: "))
    calcular=notapractica+notateorica/2
    
    

    # Calcular el promedio
    promedio = calcular(notateorica, notapractica)

    # Actualizar el estado del camper según el promedio
    if promedio >= 60:
        camper_encontrado["Estado"] = "Aprobado"
        print(f"Camper {camper_encontrado['Nombres']} {camper_encontrado['Apellido']} ha sido aprobado.")
    else:
        camper_encontrado["Estado"] = "Reprobado"
        print(f"Camper {camper_encontrado['Nombres']} {camper_encontrado['Apellido']} ha sido reprobado.")

    # Guardar los cambios en el archivo JSON
    guardarJSON({"campers": campers_list})
>>>>>>> 0e4af4b (Programa funcional)
