
import subprocess #Esto nos servirá para poder ejecutar el modo multijugador
import sys

from game_logic import jugar_solo  # Importamos la funcion del otro archivo

# Aqui se ve la bienvenida del juego
print("================================")
print("       SABE O NO SABE")
print("================================")

print("Bienvenido a nuestro juego")

print("\nSeleccione el modo de juego")
print("1. Local")
print("2. Lan")

modo = input("Elige una opcion: ")

# Si elige 1, empieza el juego para la unica persona
if modo == "1":

    jugar_solo()

# Si elige 2, se inicia el cliente para jugar por LAN, osea que inicia el modo multijugador
elif modo == "2":

    print("\nIniciando modo multijugador")
    print("Conectando con el servidor...")

    # Ejecuta el archivo cliente.py utilizando el mismo Python
    subprocess.run([sys.executable, "cliente.py"])

else:

    print("Opcion no valida")

# Es el ultimo mensaje que recibe el jugador cuando se acaba el juego
print("\nGracias por jugar Sabe o No Sabe")
