import socket
import json

PUERTO = 5000  # Puerto donde el cliente busca al servidor.


# Estas funciones convierten los datos a JSON para enviarlos y volverlos a leer al recibirlos.
def enviar(conexion, datos):
    mensaje = json.dumps(datos) + "\n"
    conexion.sendall(mensaje.encode("utf-8"))


def recibir(archivo):
    mensaje = archivo.readline()
    if not mensaje:
        raise ConnectionError("Se perdio la conexion")
    return json.loads(mensaje)


# Muestra el título y solicita el nombre del jugador y la IP del servidor.
print("================================")
print("       CLIENTE DEL JUEGO")
print("================================")
nombre = input("Escribe tu nombre: ")
ip = input("Escribe la IP del servidor: ")

conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
archivo = None

try:
    # Abre la conexión, prepara la lectura de mensajes y envía el nombre al servidor.
    conexion.connect((ip, PUERTO))
    archivo = conexion.makefile("r", encoding="utf-8")
    enviar(conexion, {"nombre": nombre})
    print("\nConectado correctamente")

    # Espera mensajes del servidor y realiza una acción según el tipo recibido.
    while True:
        datos = recibir(archivo)

        if datos["tipo"] == "esperando":
            # El servidor aún espera; muestra el aviso que envió.
            print(datos["mensaje"])

        elif datos["tipo"] == "inicio":
            # Informa que comenzó la partida y muestra la categoría seleccionada.
            print("\nLa partida ha comenzado")
            if datos["categoria"] == "1":
                print("Categoria: Cultura General")
            else:
                print("Categoria: Ingenieria en Sistemas")

        elif datos["tipo"] == "pregunta":
            # Muestra la pregunta y enumera sus opciones para que el jugador elija.
            print("\nPregunta", datos["numero"])
            print(datos["texto"])
            for i, opcion in enumerate(datos["opciones"], 1):
                print(str(i) + ".", opcion)

            # Repite la solicitud hasta recibir una opción del 1 al 4 y la envía.
            respuesta = input("Turno de " + nombre + ": ")
            while respuesta not in ["1", "2", "3", "4"]:
                print("Respuesta no valida")
                respuesta = input("Selecciona del 1 al 4: ")
            enviar(conexion, {"respuesta": respuesta})

        elif datos["tipo"] == "resultado":
            # Muestra el resultado de la respuesta y el puntaje acumulado.
            print(datos["mensaje"])
            print("Puntos actuales:", datos["puntos"])

        elif datos["tipo"] == "final":
            # Presenta el puntaje final y termina el ciclo de espera.
            print("\nRESULTADOS FINALES")
            print(nombre, "obtuvo", datos["puntos"], "puntos de 10")
            break

except (ConnectionError, OSError, ValueError) as error:
    # Si falla la conexión o la lectura de datos, muestra el motivo del error.
    print("Error de conexion:", error)

finally:
    # Cierra los recursos de red al terminar, haya ocurrido un error o no.
    if archivo is not None:
        archivo.close()
    conexion.close()
    print("\nConexion cerrada")
