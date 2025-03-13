# Clase persona

class Persona:

    # método constructor
    def __init__(self, nombre, apellido, edad):
        self.Nombre = nombre
        self.Apellido = apellido
        self.Edad = edad
    
    # método para mostrar los datos de una persona
    def MostrarPersona(self):
        print("Nombre: " + self.Nombre)
        print("Apellido: " + self.Apellido)
        print("Edad: " + str(self.Edad))

# método principal
def main():
    p1 = Persona("Maria", "Duque", 16)
    p1.MostrarPersona()
    p2 = Persona("Erika", "González", 34)
    p2.MostrarPersona()
    p1.Edad = 20
    p1.MostrarPersona()
    p1 = p2
    p1.MostrarPersona()
    p2.MostrarPersona()

if __name__ == "__main__":
    main()