def agregar_o_actualizar_puntaje(nombre_usuario, nombre_archivo="puntajes.txt"):
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
            print(f'Usuario {nombre_usuario} encontrado, se actualizará su puntuación')
        # Volver a unir y guardar la línea (modificada o no)
        nueva_linea = ",".join(partes) + '\n'
        datos_actualizados.append(nueva_linea)

    # Caso 2: Usuario NO ENCONTRADO -> Agregar nueva línea
    if not encontrado:
        # Se agrega el nuevo usuario al final de la lista con valores predeterminados (0,0)
        linea_nueva_usuario = f"{nombre_usuario},0,0\n"
        datos_actualizados.append(linea_nueva_usuario)
        print(f"➕ Usuario '{nombre_usuario}' no encontrado. Agregado al final con puntajes 0,0.")

    # 3. Reescribir el archivo completo con la lista de líneas actualizada
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.writelines(datos_actualizados)
        print(f"✅ Archivo '{nombre_archivo}' reescrito exitosamente con los cambios.")
    

# --- EJEMPLOS DE USO ---

# Asume que 'puntajes.txt' contiene inicialmente:
# abc,1,0
# def,2,1

# 1. ACTUALIZAR un usuario existente
agregar_o_actualizar_puntaje("dsadsadsa") 
# Salida: Usuario 'abc' encontrado. Puntaje actualizado a 50.
# Contenido final de 'puntajes.txt' tendrá: abc,50,0

# 2. AGREGAR un usuario nuevo
agregar_o_actualizar_puntaje("avc")
# Salida: Usuario 'nuevo' no encontrado. Agregado al final con puntajes 0,0.
# Contenido final de 'puntajes.txt' tendrá una línea al final como: nuevo,0,0
