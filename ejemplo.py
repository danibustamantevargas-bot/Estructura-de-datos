class Persona:
    altura: float
    def __init__(self, nombre: str, edad: int):
        self .nombre = nombre
        self .edad = edad

        def saludar(self)-> str:
return f"hola, mi nombre es {self .nombre} y tego {self .edad} años. "

@staticmethod
def esMayor():
    return none

def __str__(self)->str:
    return f"persona(nombre={self .nombre}), edad={self .edad}"

class Estudiante(Persona):
    __promedio: float

    def __init__(self, nombre: str, edad: int, carrera: str):
        super() .__init__(nombre, edad)
        self . carrera = carrera

        def estudiar(self)-> str:
            return f"{self .nombre} esta estudiando {self .carrera}." 

            def __str__(self)-> str:
                return f "estudiante(nombre={self.nombre}, edad={self.edad})", carera={self.carrera})

        def getpromedio(self)-> float
        return self. __
def setpromedio(self, __promedio: float) -> none:
    self. __promedio = __promedio

            juan = Persona("Juan", 30)
            maria = Estudiante("Maria", 22, "Ingenieria")
            print(juan.saludar())
            print(maria.saludar())
            maria.setPromedio(9.5)
            juan.altura= 1.75
            print(juan)

