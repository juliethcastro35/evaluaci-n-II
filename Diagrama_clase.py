class Persona:
    def __init__(self, nombre, nif, fecha_nac):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nac = fecha_nac

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, NIF: {self.nif}, Fecha Nac: {self.fecha_nac}"

class Jugador(Persona):
    def __init__(self, nombre, nif, fecha_nac, num_fed):
        super().__init__(nombre, nif, fecha_nac)
        self.num_fed = num_fed

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Número Federación: {self.num_fed}"

persona = Persona("julieth herrera", "98765432C", "2000-11-12")
jugador = Jugador("sandra castro", "65432198D", "1995-03-23", 5678)
print(persona.mostrar_datos())
print(jugador.mostrar_datos())