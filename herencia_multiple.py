# Herencia Múltiple

class Mamifero:
    def respirar(self):
        print("Respirando...")

class AnimalMarino:
    def nadar(self):
        print("Nadando...")

class Delfin(Mamifero, AnimalMarino):
    def comunicarse(self):
        print("Emitiendo sonidos...")
    def nombre(self):
        print("El Delfín puede estar...")
    

delfin = Delfin()
delfin.nombre()
delfin.respirar()    # Heredado de Mamifero
delfin.nadar()       # Heredado de AnimalMarino
delfin.comunicarse() # Definido en Delfin