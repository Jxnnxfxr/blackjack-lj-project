from baraja import Carta


class Jugador:
    def __init__(self, nombre: str = "Jugador") -> None:
        self.nombre = nombre
        self.mano: list[Carta] = []

    def recibir_carta(self, carta: Carta) -> None:
        """Añade una carta a la mano del jugador."""
        if carta:
            self.mano.append(carta)

    def calcular_puntuacion(self) -> int:
        """Calcula la puntuación total de la mano teniendo en cuenta el valor del As (11 o 1)."""
        puntos = 0
        as_totales = 0

        for carta in self.mano:
            puntos += carta.valor
            if carta.rango == "A":
                as_totales += 1

        # Si nos pasamos de 21 y tenemos Ases, el As pasa a valer 1 (restamos 10)
        while puntos > 21 and as_totales > 0:
            puntos -= 10
            as_totales -= 1

        return puntos

    def mostrar_mano(self) -> str:
        """Devuelve una representación en texto de las cartas del jugador."""
        cartas_str = ", ".join(str(carta) for carta in self.mano)
        return f"{self.nombre} -> Cartas: [{cartas_str}] | Puntuación: {self.calcular_puntuacion()}"

    def limpiar_mano(self) -> None:
        """Vacía la mano del jugador para una nueva ronda."""
        self.mano = []

    def __str__(self) -> str:
        return self.mostrar_mano()