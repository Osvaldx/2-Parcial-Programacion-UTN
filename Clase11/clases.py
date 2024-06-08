# OOP CLASES, SELF, FUNCIONES, ATRIBUTOS

class Alumno:
    def __init__(self, nombre: str, apellido: str, dni: int, edad: int)->None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        self.especie = "humano"
    
    def presentarse(self)->str:
        return f"Hola a todos soy {self.apellido} {self.nombre} y mi edad es {self.edad} mi dni es {self.dni}, especie : {self.especie}"

alumno_1 = Alumno("Nahuel", "Romano", "46210110", "19")
alumno_2 = Alumno("Ivo", "Saja", "47119897", "19")

alumno_2.especie = "gay"

print(alumno_1.presentarse())
print(alumno_2.presentarse())