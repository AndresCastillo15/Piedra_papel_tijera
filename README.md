# Piedra, Papel o Tijeras

Un juego clásico de **Piedra, Papel o Tijeras** donde puedes jugar contra la computadora. El juego es simple y directo, perfecto para principiantes.

## Descripción

Este juego permite al jugador elegir entre **Piedra**, **Papel** o **Tijeras** mediante números, y la computadora elige una opción aleatoria. El jugador gana según las reglas tradicionales de este juego clásico:

- **Piedra** vence a **Tijeras**
- **Tijeras** vencen a **Papel**
- **Papel** vence a **Piedra**

El jugador selecciona una opción numérica:

- **1** = Piedra
- **2** = Papel
- **3** = Tijeras

## Proceso

La computadora elige aleatoriamente un número entre 1 y 3 utilizando el módulo **`random`** de Python, que se encarga de generar un número aleatorio para simular la elección de la CPU.

### Ejemplo del proceso

1. El jugador elige un número entre 1 y 3.
2. La computadora también genera un número aleatorio entre 1 y 3.
3. Se comparan ambas elecciones y el resultado se muestra.

![Diagrama de flujo](diagrama.png)
