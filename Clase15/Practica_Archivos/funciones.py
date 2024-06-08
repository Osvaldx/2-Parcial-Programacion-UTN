lista_numeros = [1,2,3,4,5,6,7,8,9,10]

# 1
def guardar_lista(lista: list, path: str)->None:
    """Esta función recibe como parámetros una lista y un path de tipo string y se encarga de abrir un archivo o crearlo en caso de no existir y recorre la lista para poder escribirla en el archivo

    Argumentos:
        lista (list): Una lista ya predefinida
        path (str): Un string ya predefinida
    """
    with open(path, "w") as archivo:
        for i in range(len(lista)):
            archivo.write(f"{lista[i]},")

# guardar_lista(lista_numeros, "Clase15/Practica_Archivos/textos/lista_numeros.txt")

# 2
def numeros_multiplos(path: str)->None:
    """Esta función recibe como parámetros un path de tipo string y se encarga de leer un archivo para después recorrer el texto de números y solo guardar los números múltiplos de 2

    Argumentos:
        path (str): Un string ya predefinida
    """
    lista_multiplos = []

    with open(path, "r") as archivo:
        numeros = archivo.readline()
        numeros = numeros.split(",")
        for i in range(len(numeros) - 1):
            if numeros[i].isnumeric() == True:
                numero = int(numeros[i])
                if numero % 2 == 0:
                    lista_multiplos.append(numero)
        print(f"Numeros multiplos de 2 {lista_multiplos}")

# numeros_multiplos("Clase15/Practica_Archivos/textos/lista_numeros.txt")

# 3
def transcribir(path_uno: str, path_dos: str)->None:
    """Esta función recibe como parámetros path uno y path dos y se encarga de transcribir lo que se encuentre en path uno hacia el path 2

    Argumentos:
        path_uno (str): Un string ya predefinida
        path_dos (str): Un string ya predefinida
    """
    texto = ""
    mensaje = ""
    extension = path_uno.split(".")
    if extension[1] == "txt":
        with open(path_uno, "r", encoding="UTF-8") as archivo:
            if archivo.readlines() != []:
                archivo.seek(0)
                texto = archivo.readlines()
                extension = path_dos.split(".")
                if extension[1] == "txt":
                    with open(path_dos, "r+", encoding="UTF-8") as archivo2:
                        archivo2.writelines(texto)
                        mensaje = "ARCHIVO TRANSCRIPTO CON EXITO"
                else:
                    mensaje = "[ERROR] El archivo no es .txt"
            else:
                mensaje = "[ERROR] El archivo esta vacio"
    
    return mensaje

# transcribir("Clase15/Practica_Archivos/textos/poema.txt", "Clase15/Practica_Archivos/textos/copia_poema.txt")
# 4
def contar_elementos(path: str):
    """Esta función recibe como parámetros un path de tipo string y se encarga de leer el archivo y sacar la cantidad de líneas, palabras y caracteres que se encuentran
    
    Argumentos:
    path (str): Un string ya predefinida
    """
    cantidad_lineas = 0
    cantidad_palabras = 0
    cantidad_caracteres = 0

    with open(path, "r", encoding="UTF-8") as archivo:
        texto = archivo.readlines()
        cantidad_lineas += len(texto)

        for linea in texto:
            lineas = linea
            cantidad_caracteres += len(lineas)
    
    with open(path, "r", encoding="UTF-8") as archivo:
        texto = archivo.read()
        texto = texto.split()
        cantidad_palabras += len(texto)
    
    print(f"""
- Cantidad de lineas: {cantidad_lineas}
- Cantidad de palabras: {cantidad_palabras}
- Cantidad de caracteres: {cantidad_caracteres}
""")

# contar_elementos("Clase15/Practica_Archivos/textos/poema.txt")