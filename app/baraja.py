import random


class Carta:
    PALOS = ("Corazones", "Diamantes", "Tréboles", "Picas")
    VALORES = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    def __init__(self, rango: str, palo: str) -> None:
        if rango not in self.VALORES:
            raise ValueError(f"Rango de carta no válido: {rango}")
        if palo not in self.PALOS:
            raise ValueError(f"Palo no válido: {palo}")
        self.rango = rango
        self.palo = palo
        self.valor = self.VALORES[rango]

    def __str__(self) -> str:
        return f"{self.rango} de {self.palo}"

    def __repr__(self) -> str:
        return f"Carta(rango={self.rango!r}, palo={self.palo!r})"


class Baraja:
    def __init__(self, barajar_al_inicio: bool = True) -> None:
        self.cartas: list[Carta] = []
        self.crear_baraja()
        if barajar_al_inicio:
            self.barajar()

    def crear_baraja(self) -> None:
        """Genera una baraja estándar de 52 cartas."""
        self.cartas = [
            Carta(rango, palo)
            for palo in Carta.PALOS
            for rango in Carta.VALORES
        ]

    def barajar(self) -> None:
        """Mezcla aleatoriamente las cartas actuales de la baraja."""
        random.shuffle(self.cartas)

    def repartir(self) -> Carta | None:
        """Saca y devuelve la última carta de la baraja. Devuelve None si está vacía."""
        if not self.cartas:
            return None
        return self.cartas.pop()

    def cartas_restantes(self) -> int:
        """Devuelve cuántas cartas quedan en la baraja."""
        return len(self.cartas)

    def __len__(self) -> int:
        return len(self.cartas)

    def __str__(self) -> str:
        return f"Baraja con {len(self.cartas)} cartas"