########################################################################################

# .strip() ______________________________________________________________
# El método strip eliminará todos los caracteres vacíos (por default) que pueda contener la variable
cadena = "##Hola mundo##"
print(cadena)
cadena = cadena.strip("#")
print(cadena)
print("--------------------------------------")
# RESULT: "Hola Mundo"

########################################################################################

# .upper() ______________________________________________________________
# El método upper convertirá a las letras en mayúsculas.
cadena = "Hola"
print(cadena)
cadena = cadena.upper()
print(cadena)
print("--------------------------------------")
# RESULT: "HOLA"

########################################################################################

# .lower() ______________________________________________________________
# El metodo lower convertira a las letras en minusculas.
cadena = "HOLA"
print(cadena)
cadena = cadena.lower()
print(cadena)
print("--------------------------------------")
# RESULT: "hola"

########################################################################################

# .capitalize() ______________________________________________________________
# El método capitalize convertirá a la primera letra de la cadena en mayúscula y el resto en minúscula.
cadena = "hola MUNDO"
print(cadena)
cadena = cadena.capitalize()
print(cadena)
print("--------------------------------------")
#

########################################################################################

# .replace() ______________________________________________________________
# El método replace remplazará un conjunto de caracteres por otro.
cadena = "Hola Mundo"
print(cadena)
cadena = cadena.replace("la", "@")
print(cadena)
print("--------------------------------------")
# RESULT: "Ho@ Mundo"

########################################################################################

# .split() ______________________________________________________________
# El método split divide una cadena en subcadenas y las devuelve almacenadas en una lista.
cadena = "Python,Java,C"
print(cadena)
cadena = cadena.split(",")
print(cadena)
print("--------------------------------------")


########################################################################################

# .join() ______________________________________________________________
# El método join devuelve la primera cadena unida a cada uno de los elementos de la lista que se le pasa como parámetro.
cadena = " | "
print(cadena)
cadena = cadena.join(['Python', 'Java', 'C'])
print(cadena)
print("--------------------------------------")


########################################################################################

# .zfill() ______________________________________________________________
# El método zfill rellena la cadena con ceros a la izquierda hasta llegar a la longitud pasada como parámetro.
cadena = "Hola"
print(cadena)
cadena = cadena.zfill(8)
print(cadena)
print("--------------------------------------")


########################################################################################

# .isalpha() ______________________________________________________________
# El método isalpha devuelve True si todos los caracteres son alfabéticos, False de lo contrario.
cadena = "Hola"
print(cadena)
cadena = cadena.isalpha()
print(cadena)
print("--------------------------------------")


########################################################################################

# .isnumeric() ______________________________________________________________
# El metodo isnumeric devuelve True si todos los caracteres son numeros, False de lo contrarior
cadena = "123"
print(cadena)
cadena = cadena.isnumeric()
print(cadena)
print("--------------------------------------")


########################################################################################

# .count() ______________________________________________________________
# El método count permite contar las veces que otra cadena se encuentra dentro de la primera.
cadena = "pedro pedro pedro pedro pe"
print(cadena)
cadena = cadena.count("pe")
print(cadena)
print("--------------------------------------")


########################################################################################

# .format() ______________________________________________________________
# En el método format las llaves, llamadas campos de formato, son reemplazadas con los valores de las variables pasadas.
nombre = "Juan"
edad = "35"
cadena = "El nombre es: {1} y su edad es: {0}"
print(cadena)
cadena = cadena.format(edad, nombre)
print(cadena)
print("--------------------------------------")


########################################################################################