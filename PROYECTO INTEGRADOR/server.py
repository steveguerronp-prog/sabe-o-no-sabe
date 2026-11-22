import socket
import json

from game_logic import obtener_preguntas, comprobar_respuesta

HOST = "0.0.0.0"  # Permite que otros equipos de la red se conecten al servidor.
PUERTO = 5000  # Puerto por el que se comunicarán clientes y servidor.


# Envía y recibe mensajes en formato JSON a través de la conexión.
def enviar(conexion, datos):
    mensaje = json.dumps(datos) + "\n"
    conexion.sendall(mensaje.encode("utf-8"))


def recibir(archivo):
    mensaje = archivo.readline()
    if not mensaje:
        raise ConnectionError("Jugador desconectado")
    return json.loads(mensaje)


# Prepara el servidor para aceptar conexiones entrantes.
print("================================")
print("       SERVIDOR DEL JUEGO")
print("================================")
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST, PUERTO))
servidor.listen(2)
print("Servidor iniciado")
print("Esperando jugadores...")

jugadores = []

try:
    # Acepta a dos jugadores, recibe sus nombres y guarda sus conexiones y puntajes.
    for i in range(2):
        conexion, direccion = servidor.accept()
        archivo = conexion.makefile("r", encoding="utf-8")
        datos = recibir(archivo)
        nombre = datos["nombre"]
        jugadores.append({
            "conexion": conexion,
            "archivo": archivo,
            "nombre": nombre,
            "puntos": 0
        })
        print(nombre, "se ha conectado")
        enviar(conexion, {
            "tipo": "esperando",
            "mensaje": "Esperando al segundo jugador"
        })

    print("\nLos dos jugadores estan conectados")

    # Pide una categoría válida y obtiene las preguntas correspondientes.
    print("\nSeleccione una categoria")
    print("1. Cultura general")
    print("2. Ingenieria en Sistemas")
    categoria = input("Escribe la categoria: ")
    while categoria not in ["1", "2"]:
        print("Opcion no valida")
        categoria = input("Escribe la categoria: ")

    if categoria == "1":
        print("Elegiste Cultura General")
    else:
        print("Elegiste Ingenieria en Sistemas")

    preguntas = obtener_preguntas(categoria)

    # Avisa a ambos clientes que la partida comienza y comunica la categoría.
    for jugador in jugadores:
        enviar(jugador["conexion"], {
            "tipo": "inicio",
            "categoria": categoria
        })

    numero = 1

    # Recorre las preguntas; ambos jugadores reciben la misma pregunta en cada ronda.
    for pregunta in preguntas:
        print("\nPregunta", numero, ":", pregunta[0])

        for jugador in jugadores:
            enviar(jugador["conexion"], {
                "tipo": "pregunta",
                "numero": numero,
                "texto": pregunta[0],
                "opciones": pregunta[1]
            })

        # Recibe cada respuesta, comprueba si es correcta y actualiza el puntaje.
        for jugador in jugadores:
            respuesta = recibir(jugador["archivo"])
            respuesta = respuesta["respuesta"]

            if comprobar_respuesta(respuesta, pregunta):
                jugador["puntos"] += 1
                mensaje = "Respuesta correcta"
            else:
                mensaje = "Respuesta incorrecta"

            # Envía al jugador el resultado de la respuesta y sus puntos actuales.
            enviar(jugador["conexion"], {
                "tipo": "resultado",
                "mensaje": mensaje,
                "puntos": jugador["puntos"]
            })
            print(jugador["nombre"], ":", mensaje)

        numero += 1

    # Envía los puntajes finales y anuncia quién ganó o si hubo empate.
    print("\nRESULTADOS FINALES")
    for jugador in jugadores:
        enviar(jugador["conexion"], {
            "tipo": "final",
            "puntos": jugador["puntos"]
        })
        print(jugador["nombre"], "obtuvo", jugador["puntos"], "puntos")

    if jugadores[0]["puntos"] > jugadores[1]["puntos"]:
        print("El ganador es", jugadores[0]["nombre"])
    elif jugadores[1]["puntos"] > jugadores[0]["puntos"]:
        print("El ganador es", jugadores[1]["nombre"])
    else:
        print("Hay un empate")

except (ConnectionError, OSError, KeyError, ValueError) as error:
    # Informa si se pierde una conexión o si ocurre un error de datos o del sistema.
    print("Error en el servidor:", error)

finally:
    # Cierra las conexiones de los jugadores y el servidor al terminar.
    for jugador in jugadores:
        jugador["archivo"].close()
        jugador["conexion"].close()
    servidor.close()
    print("\nServidor cerrado")
