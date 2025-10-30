import os
os.system("cls")

class Persona:
    def __init__(self, nombre, nif, fecha_nac ):
        self.nombre = nombre
        self.nif = nif 
        self.fecha_nac = fecha_nac
    
    def mostrar_info(self):
        print(f"🔠Nombre: {self.nombre}")
        print(f"NIF: {self.nif}")
        print(f"📩Fecha de nacimeiento:{self.fecha_nac}")
        
    
class Jugador(Persona):   
    def __init__(self, nombre, nif, fecha_nac, num_fed):
        super().__init__(nombre, nif, fecha_nac)
        self.num_fed = num_fed
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Federación: {self.num_fed}")
if __name__ == "__main__":
    jugador1 = Jugador("Juan Esteban", "12345678", "2002-05-10", 11)
    jugador1.mostrar_info()

if __name__ == "__main__":
    jugador2 = Jugador("Isabela Alzate", "10548656676", "2007-01-11", 17)
    jugador2.mostrar_info() 

        
        