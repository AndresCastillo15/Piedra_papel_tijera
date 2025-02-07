import random

# Mostrar las opciones de forma amigable
print("╔══════════════════╗")
print("1 = Piedra")
print("2 = Papel")
print("3 = Tijeras")
print("╚══════════════════╝")

# Pedir la elección del jugador
print("╔═══════════════════════════════════╗")
opcion = input("Elige una opción (1-3): ")
opcion = int(opcion)
print("╚═══════════════════════════════════╝")

# Verificar si la opción es válida
if opcion < 1 or opcion > 3:
    print("Opción no válida. Por favor elige un número entre 1 y 3.")
else:
    # Opciones disponibles
    opciones = ["piedra", "papel", "tijeras"]

    # Selección aleatoria de la computadora
    eleccion_computadora = random.choice(opciones)

    # Convertir la elección del jugador en texto
    if opcion == 1:
        eleccion_jugador = "piedra"
    elif opcion == 2:
        eleccion_jugador = "papel"
    else:
        eleccion_jugador = "tijeras"

    # Mostrar las elecciones
    print("╔═══════════════════════════════════╗")
    print(f"Tu elección: {eleccion_jugador}")
    print(f"La computadora eligió: {eleccion_computadora}")
    print("╚═══════════════════════════════════╝")

    # Determinar el ganador
    if eleccion_jugador == eleccion_computadora:
        print("¡Es un empate!")
    elif (eleccion_jugador == "piedra" and eleccion_computadora == "tijeras") or \
         (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or \
         (eleccion_jugador == "tijeras" and eleccion_computadora == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
