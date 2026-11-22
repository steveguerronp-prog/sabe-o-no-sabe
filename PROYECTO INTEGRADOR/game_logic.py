
import random #esto nos servirá para que las preguntas sean en desorden


# bancos de preguntas cultura general

def obtener_preguntas(categoria):

    if categoria == "1":

        preguntas = [
            ["¿Cuál es la capital de Ecuador?", ["Lima", "Quito", "Bogota", "Santiago"], "2"],
            ["¿Cuántos días tiene una semana?", ["5", "6", "7", "8"], "3"],
            ["¿Cuál es el planeta más grande?", ["Marte", "Venus", "Tierra", "Jupiter"], "4"],
            ["¿Cuántos meses tiene un año?", ["10", "11", "12", "13"], "3"],
            ["¿Cuál es el océano más grande?", ["Atlantico", "Indico", "Pacifico", "Artico"], "3"],
            ["¿Qué animal es el rey de la selva?", ["Leon", "Tigre", "Elefante", "Jirafa"], "1"],
            ["¿Cuántas patas tiene una araña?", ["6", "8", "10", "4"], "2"],
            ["¿En qué continente está Ecuador?", ["Europa", "Asia", "Africa", "America"], "4"],
            ["¿Cuál es el satélite natural de la Tierra?", ["Sol", "Luna", "Marte", "Venus"], "2"],
            ["¿Cuánto es 5 x 5?", ["20", "30", "25", "15"], "3"],
            ["¿Qué idioma se habla en Brasil?", ["Español", "Ingles", "Frances", "Portugues"], "4"],
            ["¿Cuál es el animal más alto?", ["Caballo", "Jirafa", "Cebra", "Leon"], "2"],
            ["¿Cuántos colores tiene el arcoiris?", ["5", "6", "7", "8"], "3"],
            ["¿Qué estrella ilumina la Tierra?", ["Luna", "Venus", "Marte", "Sol"], "4"],
            ["¿En qué país están las pirámides de Giza?", ["Egipto", "Mexico", "Italia", "China"], "1"]
        ]
 #Banco de preguntas temática ingeniería en sistemas
    elif categoria == "2":

        preguntas = [
            ["¿Qué significa CPU?", ["Unidad Central de Procesamiento", "Control Principal Universal", "Centro de Programacion Unico", "Unidad de Computadora Personal"], "1"],
            ["¿Qué es Python?", ["Sistema operativo", "Lenguaje de programacion", "Computadora", "Navegador"], "2"],
            ["¿Qué significa RAM?", ["Red de acceso mundial", "Unidad de almacenamiento", "Memoria de acceso aleatorio", "Sistema operativo"], "3"],
            ["¿Qué es un teclado?", ["Dispositivo de salida", "Programa", "Procesador", "Dispositivo de entrada"], "4"],
            ["¿Para qué sirve un mouse?", ["Imprimir documentos", "Mover el cursor", "Guardar archivos", "Apagar la computadora"], "2"],
            ["¿Qué significa USB?", ["Universal Serial Bus", "Unidad de Sistema Basico", "Usuario de Sistema Base", "Unidad de Software Basico"], "1"],
            ["¿Qué es un monitor?", ["Dispositivo de entrada", "Procesador", "Dispositivo de salida", "Memoria"], "3"],
            ["¿Qué es Internet?", ["Un videojuego", "Un teclado", "Un programa de dibujo", "Una red mundial"], "4"],
            ["¿Qué significa LAN?", ["Lenguaje automatico", "Red de area local", "Linea nacional", "Memoria local"], "2"],
            ["¿Qué es un archivo?", ["Componente fisico", "Cable", "Conjunto de datos", "Procesador"], "3"],
            ["¿Qué significa HTML?", ["Lenguaje de marcado de hipertexto", "Memoria", "Sistema operativo", "Tipo de computadora"], "1"],
            ["¿Qué es un sistema operativo?", ["Programa para dibujar", "Dispositivo", "Navegador web", "Software que administra la computadora"], "4"],
            ["¿Cuál es un navegador web?", ["Microsoft Word", "Google Chrome", "Calculadora", "Paint"], "2"],
            ["¿Qué es un virus informático?", ["Parte del teclado", "Tipo de monitor", "Programa malicioso", "Sistema operativo"], "3"],
            ["¿Para qué sirve una impresora?", ["Escuchar musica", "Navegar por Internet", "Guardar archivos", "Imprimir documentos"], "4"]
        ]

    else:
        print("Categoria no valida")
        return [] #Esta parte de aquí lo que hace es que si meten un valor que no sea 1 o 2 cree una lista vacía para que
                  #el programa no genere las preguntas alazares
    return random.sample(preguntas, 10) #Este comando lo que permite es hacer que las preguntas se escojan de forma aleatoría
                                        #y que no se repitan


# COMPROBAR SI UNA RESPUESTA ES CORRECTA

def comprobar_respuesta(respuesta, pregunta):

    if respuesta == pregunta[2]:   #Compara la respuesta del usuario con la respuesta que ya esta predeterminada
        return True
    else:
        return False


# MODO DE JUEGO INDIVIDUAL

def jugar_solo():

    print("\nSabe o No Sabe")
    print("Bienvenido a nuestro juego")

    jugador1 = input("Escribe el nombre del jugador 1: ")
    print("Bienvenido", jugador1)

    jugador2 = input("Escribe el nombre del jugador 2: ")
    print("Bienvenido", jugador2)

    puntos1 = 0
    puntos2 = 0

    print("\nSeleccione una categoria")
    print("1. Cultura general")
    print("2. Ingenieria en Sistemas")

    categoria = input("¡Escoge la temática! (únicamente el número): ")

    if categoria == "1":
        print("Elegiste Cultura General")

    elif categoria == "2":
        print("Elegiste Ingenieria en Sistemas")

    else:
        print("Opcion no valida")
        return #DETIENE LA FUNCION SI NO INGRESAN NI 1 NI 2

    preguntas = obtener_preguntas(categoria)

    numero = 1

    for pregunta in preguntas:

        print("\nPregunta", numero, ":", pregunta[0]) #Muestra la pregunta

        print("1.", pregunta[1][0])
        print("2.", pregunta[1][1]) #Muestra el las respuestas de la lista interna
        print("3.", pregunta[1][2])
        print("4.", pregunta[1][3])

        respuesta = input("Turno de " + jugador1 + ": ")

        while respuesta not in ["1", "2", "3", "4"]:
            print("Respuesta no valida")                   #bucle para evitar una respuesta menor a 0 o mayor a 4
            respuesta = input("Selecciona del 1 al 4: ")   

        if comprobar_respuesta(respuesta, pregunta):
            print("Correcto")                          
            puntos1 += 1
        else:
            print("Respuesta incorrecta")

        respuesta = input("Turno de " + jugador2 + ": ")

        while respuesta not in ["1", "2", "3", "4"]:
            print("Respuesta no valida")
            respuesta = input("Selecciona del 1 al 4: ")

        if comprobar_respuesta(respuesta, pregunta):
            print("Correcto")
            puntos2 += 1
        else:
            print("Respuesta incorrecta")

        numero += 1
 #ESTA ES LA COMPARACIÓN DE PUNTAJES Y SE DETERMINA EL GANADOR
    print("\nResultados")
    print(jugador1, "obtuvo", puntos1, "puntos")
    print(jugador2, "obtuvo", puntos2, "puntos")

    if puntos1 > puntos2:
        print("El ganador es", jugador1)

    elif puntos2 > puntos1:
        print("El ganador es", jugador2)

    else:
        print("Hay un empate")
