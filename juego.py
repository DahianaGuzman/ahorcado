def menu():
    print('''
.----------------------------------.
|     CATEGORÍAS DISPONIBLES       |
|----------------------------------|
| 0 | Ver el top de puntuaciones   |
| 1 | frutas                       |
| 2 | paises                       |
| 3 | animales                     |
| 4 | deportes                     |
| 5 | profesiones                  |
| 6 | tecnologia                   |
| 7 | cine                         |
| 8 | cosas_de_la_casa             |
| 9 | partes_del_cuerpo            |
| 10| universo                     |
| 11| mitologia                    |
| 12| videojuegos                  |
| 13| comida                       |
| 14| instrumentos_musicales       |
\'----------------------------------\'''')
    opcion = int(input('Ingrese número de categoria: '))
    while opcion > 14 or opcion < 0:
        print('Ingrese un número de categoría válido')
        opcion = int(input('Ingrese número de categoria: '))
    return opcion

def gestionar_jugador(nombre_usuario, nombre_archivo="puntajes.txt"):
    """
    Busca al usuario en el archivo. Si lo encuentra, actualiza su puntaje.
    Si no lo encuentra, lo agrega al final con puntaje 0,0.
    """
    
    # 1. Leer todo el contenido del archivo
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    # 2. Intentar modificar la línea deseada en memoria
    datos_actualizados = []
    encontrado = False

    for linea in lineas:
        linea_limpia = linea.strip()
        partes = linea_limpia.split(',')
        
        if partes and partes[0] == nombre_usuario:
            # Caso 1: Usuario ENCONTRADO -> Actualizar puntaje
            encontrado = True
            print(f'Usuario {nombre_usuario} encontrado, se actualizará su puntuación\n')
        # Volver a unir y guardar la línea (modificada o no)
        nueva_linea = ",".join(partes) + '\n'
        datos_actualizados.append(nueva_linea)

    # Caso 2: Usuario NO ENCONTRADO -> Agregar nueva línea
    if not encontrado:
        # Se agrega el nuevo usuario al final de la lista con valores predeterminados (0,0)
        linea_nueva_usuario = f"{nombre_usuario},0,0\n"
        datos_actualizados.append(linea_nueva_usuario)
        print(f"\n➕ Usuario '{nombre_usuario}' no encontrado. Agregado al final con puntajes 0,0.\n")

    # 3. Reescribir el archivo completo con la lista de líneas actualizada
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.writelines(datos_actualizados)

def actualizar_puntajes(apodo, gano=False, perdio=False, nombre_archivo="puntajes.txt"):
    """
    Busca al jugador y suma 1 a las victorias si gano=True, o a las derrotas si perdio=True.
    Si no lo encuentra, lo agrega con el puntaje inicial 1,0 (si gano) o 0,1 (si perdio) o 0,0.
    """
    
    # Leer todo el contenido del archivo

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()


    # Modificar la línea deseada en memoria
    datos_actualizados = []
    encontrado = False

    for linea in lineas:
        linea_limpia = linea.strip()
        partes = linea_limpia.split(',')
        
        if partes and partes[0] == apodo:
            encontrado = True
            
            # Sumar 1 a las VICTORIAS (índice 1)
            if gano:
                victorias_actuales = int(partes[1])
                partes[1] = str(victorias_actuales + 1)
                print(f"🏆 ¡{apodo} ganó! Victorias actualizadas: {victorias_actuales} -> {victorias_actuales + 1}.")

            # Sumar 1 a las DERROTAS (índice 2)
            elif perdio:
                derrotas_actuales = int(partes[2])
                partes[2] = str(derrotas_actuales + 1)
                print(f"😔 {apodo} perdió. Derrotas actualizadas: {derrotas_actuales} -> {derrotas_actuales + 1}.")
            
        # Volver a unir y guardar la línea (modificada o no)
        nueva_linea = ",".join(partes) + '\n'
        datos_actualizados.append(nueva_linea)

    # Reescribir el archivo completo
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.writelines(datos_actualizados)

def top():
    archivo = open('puntajes.txt', 'r', encoding='utf-8')
    lineas = archivo.readlines()
    print('\n##TOP PUNTUACIONES##')
    for linea in lineas[:10]:
        print(linea.strip())

# Lista que contiene las 7 fases (de 0 a 6 intentos fallidos)
FASES_AHORCADO = [
    # 0 Intentos fallidos (Inicio)
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    # 1 Intento fallido (Cabeza)
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    # 2 Intentos fallidos (Cuerpo)
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    # 3 Intentos fallidos (Brazo Izquierdo)
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    """,
    # 4 Intentos fallidos (Brazo Derecho)
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    """,
    # 5 Intentos fallidos (Pierna Izquierda)
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    """,
    # 6 Intentos fallidos (Fin del juego - Pierna Derecha)
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    """
]

def imprimir_ahorcado(intentos_fallidos):
    """
    Imprime la fase del ahorcado correspondiente al número de intentos fallidos.
    """
    # Aseguramos que el índice esté dentro del rango (0 a 6)
    indice = min(intentos_fallidos, 6)
    print(FASES_AHORCADO[indice])

def jugar_partida(opcion, apodo):
    if opcion == 0:
        top()
    else:
        gestionar_jugador(apodo)
        import random

        # Abrir el archivo
        archivo = open("palabras.txt", "r", encoding="utf-8")

        categorias = []      # lista vacía para guardar todo
        categoria = ""        # variable temporal
        lista_palabras = []   # variable temporal

        # Recorrer línea por línea
        for linea in archivo:
            linea = linea.strip()   # Quita los saltos de línea

            # Si la línea empieza con "categoria:", imprimimos el nombre
            if linea.startswith("categoria:"):                 #.starwitch: una cadena comienza con cierto texto?
                categoria = linea.replace("categoria:", "")    #.replace reemplaza una parte del texto pot otra categoria lo remplaza por "" nada, asi que solo queda la otra palabra
                #print("\nCategoría:", categoria)  ya no la necesito

            elif linea != "":
                # Convertimos la línea en una lista usando split
                lista_palabras = linea.split(",")              #corta el texto cada vez que encuentra una coma y crea una lista. Ejem:"pera,banano" da ["pera", "banano"].
                categorias.append([categoria, lista_palabras]) #se usa la lista categorias para crear una lista anidada con todas las categorias y sus elementos

        # Cerrar el archivo
        archivo.close()

        categoria_elegida = categorias[opcion - 1][0]      #cabeza de la sublista 
        palabras_categoria = categorias[opcion - 1][1]     #cola de la sublista, resto de elementos

        print("\nElegiste la categoría:", categoria_elegida)

        palabra_secreta = random.choice(palabras_categoria)                 #elige un elemento al azar de la lista.
        #print("Palabra secreta:", palabra_secreta)                         (solo para prueba)

        oculta = ["_"] * len(palabra_secreta)   #crea un guion por cada letra 
        acierto= False                          #BANDERA para poder notificiar al usuario si acerto
        intentos = 6           #graduar el limite de intentos permitidos    
        letras_usadas = []     #evitar que el usuario repita letras

        #mientras haya intentos y queden letras por adivinar
        while intentos > 0 and "_" in oculta:
            print("\nPalabra:", " ".join(oculta))  #se le agrega espacios con .join entre cada elemento (en este caso los guiones)
            print("Intentos restantes:", intentos)
            imprimir_ahorcado(intentos_fallidos=6-intentos)


            letra = input("Adivina una letra: ").lower()

            # Si la letra ya fue usada, saltar
            if letra in letras_usadas:
                print("Ya usaste esa letra. Intenta otra.")
                continue                        #salta al siguiente ciclo si repite una letra.

            letras_usadas.append(letra)
            acierto = False

            #se verifica si la letra ingresada si se encuentra en la palabra secreta y se agrega
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    oculta[i] = letra
                    acierto = True              #si hay coincidencia, la bandera se activa

            # se crea la notificación de aciertos
            if acierto:
                print("¡Acertaste, La letra está en la palabra!")
            else:
                print("Esta letra no está :(")
                intentos -=1

            print(" ".join(oculta))

        # Fin del juego, lo completo o fallo
        if "_" not in oculta:                   #sirve para saber si aún quedan letras ocultas
            print("\n ¡Ganaste! La palabra era:", palabra_secreta)
            actualizar_puntajes(apodo, gano= True, perdio = False)
        else:
            print("\nTe quedaste sin intentos. La palabra era:", palabra_secreta)
            actualizar_puntajes(apodo, gano= False, perdio = True)
            imprimir_ahorcado(intentos_fallidos=6)

apodo = input('Ingresa tu nombre: ')

opcion = menu()

jugar_partida(opcion, apodo= apodo)




    