import random

# Saludamos al jugador
print("¡Hola! Vamos a jugar a Piedra, Papel o Tijeras.")
print("Las reglas son: Piedra vence a Tijeras, Tijeras vence a Papel, y Papel vence a Piedra.")

# Preparamos las opciones
opciones = ["Piedra", "Papel", "Tijeras"]

# Elige el jugador
eleccion_jugador = input("Elige una opción: Piedra, Papel o Tijeras: ")

# Elige la computadora
eleccion_computadora = random.choice(opciones)
print(f"La computadora eligió: {eleccion_computadora}")

# Comparamos las opciones
if eleccion_jugador == eleccion_computadora:
    print("Es un empate.")
elif (eleccion_jugador == "Piedra" and eleccion_computadora == "Tijeras") or \
     (eleccion_jugador == "Tijeras" and eleccion_computadora == "Papel") or \
     (eleccion_jugador == "Papel" and eleccion_computadora == "Piedra"):
    print("¡Ganas! :)")
else:
    print("Pierdes. La computadora gana. :(")
