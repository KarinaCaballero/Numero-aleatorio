
# Juego de adivinar el número
import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 10)

# Inicializar el contador de intentos
intentos = 0

# Mostrar un mensaje de bienvenida
print("Bienvenido al juego de adivinar el número.")
print("Tienes 10 intentos para adivinar el número secreto.")

# Repetir hasta que se acaben los intentos o se adivine el número
while intentos < 10:
    # Pedir al usuario que introduzca un número
    print("Introduce un número entre 1 y 10:")
    numero_usuario = int(input())

    # Incrementar el contador de intentos
    intentos = intentos + 1

    # Comprobar si el número del usuario es correcto, mayor o menor que el secreto
    if numero_usuario == numero_secreto:
        # Felicitar al usuario y terminar el juego
        print("¡Felicidades! Has adivinado el número en", intentos, "intentos.")
        break
    elif numero_usuario < numero_secreto:
        # Indicar al usuario que su número es menor que el secreto
        print("Tu número es menor que el número secreto.")
    else:
        # Indicar al usuario que su número es mayor que el secreto
        print("Tu número es mayor que el número secreto.")

# Si se han agotado los intentos y no se ha adivinado el número, mostrar el número secreto
if intentos == 10 and numero_usuario != numero_secreto:
    print("Lo siento, no has adivinado el número. El número secreto era", numero_secreto, ".")