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
        categorias.append([categoria, lista_palabras]) #se usa una la lista categorias para crear una lista anidada con todas las categorias y sus elementos

# Cerrar el archivo
archivo.close()


#print (categorias)

#mostrar al usuario las categorias a elegir
print("Categorías disponibles:\n")

for i in range(len(categorias)):
    print(i + 1, "-", categorias[i][0]) #imprime solo el elemento de la posicion 0 (la cabeza de la lista)

opcion = int(input("\nElige el número de la categoría: "))

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
    print("Letras usadas:", letras_usadas) #eliminar


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
else:
    print("\nTe quedaste sin intentos. La palabra era:", palabra_secreta)
