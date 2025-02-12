#APUNTES

# Nuevo diccionario con detalles de las rutas (sin capacidad ni instructor, solo los módulos)
rutas_detalles = {
    "Ruta Java": [
        "Intro",
        "Python",
        "HTML/CSS",
        "Scrum",
        "Git",
        "JavaScript",
        "Intro Back",
        "Intro BBDD",
        "MySQL",
        "Java",
        "PostgreSQL",
        "SpringBoot"
    ],
    "Ruta NodeJS": [
        "Intro",
        "Python",
        "HTML/CSS",
        "Scrum",
        "Git",
        "JavaScript",
        "Intro Back",
        "Intro BBDD",
        "MongoDB",
        "JavaScript",
        "MySQL",
        "Express"
    ],
    "Ruta .NET": [
        "Intro",
        "Python",
        "HTML/CSS",
        "Scrum",
        "Git",
        "JavaScript",
        "Intro Back",
        "Intro BBDD",
        "MySQL",
        "C#",
        "PostgreSQL",
        ".Net Core"
    ]
}

# Diccionario de campers (igual que antes)
campers = [
    {"id": 1, "Nombres": "Andres David", "Apellido": "Reyes Espinel", "Estado": "Reprobado"},
    {"id": 2, "Nombres": "Carlos Alberto", "Apellido": "Gomez Perez", "Estado": "Aprobado"},
    {"id": 3, "Nombres": "Maria Fernanda", "Apellido": "Lopez Martinez", "Estado": "Reprobado"},
    {"id": 4, "Nombres": "Juan Pablo", "Apellido": "Rodriguez Garcia", "Estado": "Aprobado"},
    {"id": 5, "Nombres": "Ana Maria", "Apellido": "Diaz Sanchez", "Estado": "Reprobado"},
    {"id": 6, "Nombres": "Luis Fernando", "Apellido": "Hernandez Gomez", "Estado": "Aprobado"},
    {"id": 7, "Nombres": "Sofia Alejandra", "Apellido": "Martinez Lopez", "Estado": "Reprobado"},
    {"id": 8, "Nombres": "Diego Alejandro", "Apellido": "Perez Diaz", "Estado": "Aprobado"},
    {"id": 9, "Nombres": "Camila Andrea", "Apellido": "Garcia Rodriguez", "Estado": "Reprobado"},
    {"id": 10, "Nombres": "Jorge Luis", "Apellido": "Sanchez Hernandez", "Estado": "Aprobado"},
    {"id": 11, "Nombres": "Laura Valentina", "Apellido": "Gomez Martinez", "Estado": "Reprobado"},
    {"id": 12, "Nombres": "Andres Felipe", "Apellido": "Lopez Garcia", "Estado": "Aprobado"},
    {"id": 13, "Nombres": "Paola Andrea", "Apellido": "Martinez Diaz", "Estado": "Reprobado"},
    {"id": 14, "Nombres": "David Santiago", "Apellido": "Rodriguez Perez", "Estado": "Aprobado"},
    {"id": 15, "Nombres": "Valentina Sofia", "Apellido": "Hernandez Lopez", "Estado": "Reprobado"},
    {"id": 16, "Nombres": "Sebastian David", "Apellido": "Garcia Sanchez", "Estado": "Aprobado"},
    {"id": 17, "Nombres": "Natalia Andrea", "Apellido": "Perez Martinez", "Estado": "Reprobado"},
    {"id": 18, "Nombres": "Juan David", "Apellido": "Diaz Rodriguez", "Estado": "Aprobado"},
    {"id": 19, "Nombres": "Andres David", "Apellido": "Reyes Espinel", "Estado": "Reprobado"},
    {"id": 20, "Nombres": "Carlos Alberto", "Apellido": "Gomez Perez", "Estado": "Aprobado"},
    {"id": 21, "Nombres": "Maria Fernanda", "Apellido": "Lopez Martinez", "Estado": "Reprobado"}
]

# Filtramos los campers aprobados
campers_aprobados = [camper for camper in campers if camper["Estado"] == "Aprobado"]

# Diccionario donde se asignarán los campers a las rutas
asignaciones = {
    "Ruta Java": [],
    "Ruta NodeJS": [],
    "Ruta .NET": []
}

# Función para asignar campers a las rutas
def asignar_camper_a_ruta(camper, rutas_detalles, asignaciones):
    for ruta in rutas_detalles:
        # Aquí podemos simplemente asignar sin limitación de capacidad, ya que no se especifica capacidad
        asignaciones[ruta].append(camper)
        print(f"{camper['Nombres']} {camper['Apellido']} asignado a la ruta {ruta}.")
        return
    print(f"No se pudo asignar a {camper['Nombres']} {camper['Apellido']}.")

# Asignar todos los campers aprobados a las rutas
for camper in campers_aprobados:
    asignar_camper_a_ruta(camper, rutas_detalles, asignaciones)

# Mostrar las asignaciones finales
print("\nAsignaciones finales:")
for ruta, campers in asignaciones.items():
    print(f"Ruta {ruta}:")
    for camper in campers:
        print(f"  - {camper['Nombres']} {camper['Apellido']}")

