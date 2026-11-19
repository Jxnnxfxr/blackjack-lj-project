from baraja import Baraja
from jugador import Jugador


class Juego:
    """Gestiona una partida de Blackjack entre un jugador y el crupier."""

    LIMITE_CRUPIER = 17
    MINIMO_CARTAS = 15  # Si quedan menos, se crea una baraja nueva

    def __init__(self, nombre_jugador: str = "Jugador") -> None:
        self.baraja = Baraja()
        self.jugador = Jugador(nombre_jugador)
        self.crupier = Jugador("Crupier")

    def comprobar_baraja(self) -> None:
        """Crea y baraja una baraja nueva si quedan pocas cartas."""
        if self.baraja.cartas_restantes() < self.MINIMO_CARTAS:
            print("\n🔄 Quedan pocas cartas. Se baraja una nueva baraja...")
            self.baraja = Baraja()

    def repartir_inicial(self) -> None:
        """Reparte dos cartas a cada uno, alternando."""
        for _ in range(2):
            self.jugador.recibir_carta(self.baraja.repartir())
            self.crupier.recibir_carta(self.baraja.repartir())

    def mostrar_mesa(self, ocultar_crupier: bool = True) -> None:
        """Muestra las manos. Si ocultar_crupier es True, solo enseña su primera carta."""
        print("\n" + "-" * 50)
        if ocultar_crupier:
            print(f"Crupier -> Cartas: [{self.crupier.mano[0]}, ??]")
        else:
            print(self.crupier.mostrar_mano())
        print(self.jugador.mostrar_mano())
        print("-" * 50)

    def turno_jugador(self) -> None:
        """El jugador pide cartas hasta plantarse o pasarse de 21."""
        while self.jugador.calcular_puntuacion() < 21:
            opcion = input("¿Quieres (p)edir carta o (s)plantarte? ").strip().lower()
            if opcion == "p":
                self.jugador.recibir_carta(self.baraja.repartir())
                self.mostrar_mesa()
            elif opcion == "s":
                break
            else:
                print("Opción no válida. Escribe 'p' o 's'.")

    def turno_crupier(self) -> None:
        """El crupier pide cartas hasta llegar al menos a 17."""
        self.mostrar_mesa(ocultar_crupier=False)
        while self.crupier.calcular_puntuacion() < self.LIMITE_CRUPIER:
            print("El crupier pide carta...")
            self.crupier.recibir_carta(self.baraja.repartir())
            self.mostrar_mesa(ocultar_crupier=False)

    def determinar_ganador(self) -> str:
        """Compara las puntuaciones y devuelve el resultado como texto."""
        puntos_jugador = self.jugador.calcular_puntuacion()
        puntos_crupier = self.crupier.calcular_puntuacion()

        if puntos_jugador > 21:
            return "💥 Te has pasado de 21. Gana el crupier."
        if puntos_crupier > 21:
            return "🎉 El crupier se ha pasado de 21. ¡Ganas tú!"
        if puntos_jugador > puntos_crupier:
            return "🎉 ¡Ganas tú!"
        if puntos_jugador < puntos_crupier:
            return "😞 Gana el crupier."
        return "🤝 Empate."

    def es_blackjack(self, participante: Jugador) -> bool:
        """Blackjack = 21 con las dos primeras cartas."""
        return len(participante.mano) == 2 and participante.calcular_puntuacion() == 21

    def jugar_ronda(self) -> None:
        """Ejecuta una ronda completa."""
        self.comprobar_baraja()
        self.jugador.limpiar_mano()
        self.crupier.limpiar_mano()

        self.repartir_inicial()
        self.mostrar_mesa()

        # Blackjack natural
        if self.es_blackjack(self.jugador) or self.es_blackjack(self.crupier):
            self.mostrar_mesa(ocultar_crupier=False)
            if self.es_blackjack(self.jugador) and self.es_blackjack(self.crupier):
                print("🤝 Los dos tenéis Blackjack. Empate.")
            elif self.es_blackjack(self.jugador):
                print("🃏 ¡BLACKJACK! ¡Ganas tú!")
            else:
                print("🃏 El crupier tiene Blackjack. Gana el crupier.")
            return

        self.turno_jugador()

        # El crupier solo juega si el jugador no se ha pasado
        if self.jugador.calcular_puntuacion() <= 21:
            self.turno_crupier()
        else:
            self.mostrar_mesa(ocultar_crupier=False)

        print(self.determinar_ganador())

    def jugar(self) -> None:
        """Bucle principal: juega rondas hasta que el jugador quiera salir."""
        while True:
            self.jugar_ronda()
            otra = input("\n¿Jugar otra ronda? (s/n): ").strip().lower()
            if otra != "s":
                print("¡Gracias por jugar!")
                break
