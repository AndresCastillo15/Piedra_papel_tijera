import random

# Elecciones
print("╔══════════════════╗")
print("1 = Piedra")
print("2 = Papel")
print("3 = Tijeras")
print("╚══════════════════╝")

print("╔═══════════════════════════════════╗")
opcion = input("Elige una opción (1-3): ")
opcion = int(opcion)
print("╚═══════════════════════════════════╝")

# Verificar si la opción es válida
maquina = random.randint(1, 3)

# Salida
if opcion < 1 or opcion > 3:
    print("Opción no válida. Por favor elige un número entre 1 y 3.")
else:
    print("El usuario escogió un valor válido")
    
    if maquina == 1:
        if opcion == 1:
            r = "Empate!"
        elif opcion == 2:
            r = "Ganaste"
        else:
            r = "Perdiste"
    elif maquina == 2:
        if opcion == 1:
            r = "Perdiste"
        elif opcion == 2:
            r = "Empate!"
        else:
            r = "Ganaste"
    else:
        if opcion == 1:
            r = "Ganaste"
        elif opcion == 2:
            r = "Perdiste"
        else:
            r = "Empate!"

    # Salida
    print("╔═══════════════════════════════════╗")
    print("═══════ " + r + " ═══════")
    print(f"Tu elección: {opcion}")
    print(f"La computadora eligió: {maquina}")
    print("╚═══════════════════════════════════╝")
