from juego import Juego


def main() -> None:
    print("=" * 50)
    print("        🃏  BIENVENIDO AL BLACKJACK  🃏")
    print("=" * 50)

    nombre = input("¿Cómo te llamas? ").strip() or "Jugador"
    juego = Juego(nombre)
    juego.jugar()


if __name__ == "__main__":
    main()
