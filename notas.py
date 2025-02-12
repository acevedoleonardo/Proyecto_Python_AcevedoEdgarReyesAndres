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

