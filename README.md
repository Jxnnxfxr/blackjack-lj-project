# blackjack-lj-project

Blackjack sencillo para consola hecho en Python. Proyecto colaborativo para practicar
programación orientada a objetos y el trabajo en equipo con Git y GitHub.

## Colaboradoras

- **@Jxnnxfxr**
- **@leticiazdp12-bit**

##  Reglas del juego

- El objetivo es acercarse lo más posible a **21** sin pasarse.
- Las cartas numéricas valen lo que indican; **J, Q y K valen 10**.
- El **As** vale 11, o 1 si con 11 te pasarías de 21.
- Al principio, el jugador y el crupier reciben 2 cartas. Una carta del crupier queda oculta.
- El jugador puede **pedir carta** o **plantarse**.
- El crupier pide carta hasta llegar como mínimo a **17**.
- Sacar 21 con las dos primeras cartas es **Blackjack**.

## Estructura del proyecto

```
blackjack-lj-project/
├── app/
│   ├── baraja.py    # Clases Carta y Baraja
│   ├── jugador.py   # Clase Jugador (mano y puntuación)
│   ├── juego.py     # Clase Juego (lógica de la partida)
│   └── main.py      # Punto de entrada
├── .gitignore
└── README.md
```

##  Cómo ejecutarlo

Necesitas **Python 3.10 o superior**, porque el código usa la sintaxis `Carta | None`.

```bash
git clone <url-del-repositorio>
cd blackjack-lj-project/app
python main.py
```

## Ramas de trabajo
| `main` | Versión estable | Ambas
| `dev`  | Versión intermedia entre las ramas de desarrollo y main | Ambas. 
| `feature/baraja-jugador` | Clases `Carta`, `Baraja` y `Jugador` | Leticia
| `feature/logica-juego` | Clase `Juego` y `main.py` | Jennifer

