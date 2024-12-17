class Persona:
    def __init__(self, nombre, presupuesto):
        """
        Constructor para inicializar el nombre y presupuesto de una persona.
        """
        self.nombre = nombre
        self.presupuesto = presupuesto

    def puede_pagar(self, costo):
        """
        Verifica si esta persona puede pagar el costo del viaje.
        """
        return self.presupuesto >= costo


def pueden_viajar(grupo, costo):
    """
    Determina si todos en el grupo pueden pagar el costo del viaje.
    :param grupo: Lista de objetos Persona.
    :param costo: Costo del viaje.
    :return: True si todos pueden pagar, False de lo contrario.
    """
    for persona in grupo:
        if not persona.puede_pagar(costo):
            print(f"{persona.nombre} no tiene suficiente dinero para el viaje.")
            return False
    return True


# Ejemplo de uso
if __name__ == "__main__":
    # Crear el grupo de amigos
    grupo = [
        Persona("Ana", 500),
        Persona("Luis", 300),
        Persona("Carla", 700),
        Persona("Jorge", 200)
    ]

    # Definir el costo del viaje
    costo_viaje = 250

    # Verificar si todos pueden viajar
    if pueden_viajar(grupo, costo_viaje):
        print("¡Todos pueden viajar juntos!")
    else:
        print("No todos pueden viajar.")

