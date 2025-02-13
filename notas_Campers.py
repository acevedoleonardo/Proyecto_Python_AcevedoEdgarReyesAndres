#Notas de Campers 

import json  # Importar el módulo json para manejar archivos JSON

def abrirJSON():
    """Función para abrir y cargar el archivo JSON."""
    try:
        with open('./campers_Bdd.json', 'r') as openFile:  # Abrir el archivo en modo lectura
            return json.load(openFile)  # Cargar y retornar el contenido del archivo
    except FileNotFoundError:
        print("Error: El archivo 'campers_Bdd.json' no existe.")
        return {"campers": []}  # Retornar un diccionario vacío si el archivo no existe

def guardarJSON(dic):
    """Función para guardar el diccionario en el archivo JSON."""
    with open('./campers_Bdd.json', 'w') as outFile:  # Abrir el archivo en modo escritura
        json.dump(dic, outFile, indent=4)  # Guardar el diccionario con formato indentado
    return True  # Retornar True para indicar que la operación fue exitosa

def ordenar():
    """Función para obtener la lista de campers desde el archivo JSON."""
    data = abrirJSON()  # Cargar los datos del archivo JSON
    return data.get("campers", [])  # Retornar la lista de campers (o una lista vacía si no existe)

def RegistrarNotas():
    """Función para registrar las notas de un camper."""
    campers_list = ordenar()  # Obtener la lista de campers
    id = int(input("Ingrese el id del camper: "))  # Solicitar el ID del camper

    # Buscar el camper por su ID
    camper_encontrado = None
    for camper in campers_list:
        if camper["id"] == id:
            camper_encontrado = camper
            break  # Salir del bucle una vez que se encuentra el camper

    if not camper_encontrado:
        print("Camper no encontrado.")
        return

    # Solicitar las notas teórica y práctica
    notateorica = float(input("Ingrese la nota teórica: "))
    notapractica = float(input("Ingrese la nota práctica: "))

    # Calcular el promedio correctamente
    promedio = (notateorica + notapractica) / 2

    # Actualizar el estado del camper según el promedio
    if promedio >= 60:
        camper_encontrado["Estado"] = "Aprobado"
        print(f"Camper {camper_encontrado['Nombres']} {camper_encontrado['Apellido']} ha sido aprobado.")
    else:
        camper_encontrado["Estado"] = "Reprobado"
        print(f"Camper {camper_encontrado['Nombres']} {camper_encontrado['Apellido']} ha sido reprobado.")

    # Actualizar las notas en el diccionario del camper
    camper_encontrado["Nota Teorica"] = notateorica
    camper_encontrado["Nota Practica"] = notapractica

    # Guardar los cambios en el archivo JSON
    guardarJSON({"campers": campers_list})

# Ejemplo de uso
if __name__ == "__main__":
    RegistrarNotas()