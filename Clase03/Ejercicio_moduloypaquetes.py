# Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

# def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
#   pass

# En donde:
# mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
# mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
# mínimo: valor mínimo admitido (inclusive)
# máximo: valor máximo admitido (inclusive) 
# reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

# En caso de que la función no haya podido conseguir un número válido, la misma retorna None.


def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int) -> int | None:
    print(mensaje)
    contador = 0

    numero = input("Ingrese un numero: ")
    numero = int(numero)
    
    while numero < minimo or numero > maximo:
        print(mensaje_error)

        if contador == reintentos:
            print("Alcanzo el maximo de intentos..")
            return None
        
        numero = int(input("Ingrese nuevamente un numero: "))
        contador += 1

    return numero

mensaje = "A continuacion ingrese un numero"
mensaje_error = "Error, su numero no se encuentra en el rango permitido"
numero_valido = get_int(mensaje, mensaje_error, 0, 10, 2)
print(numero_valido)

    

