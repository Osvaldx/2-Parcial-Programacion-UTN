# Ejercicio Integrador 01

# La división de higiene está trabajando en un control de stock para productos sanitarios.
# Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe obtener los siguientes datos:
# 	1. El tipo (validar "barbijo", "jabón" o "alcohol")
# 	2. El precio: (validar entre 100 y 300)
# 	3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000 unidades)
# 	4. La marca y el Fabricante.
  
#  Se debe informar lo siguiente:
# 	A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
# 	B. Del ingreso con más unidades, el fabricante.
# 	C. Cuántas unidades de jabones hay en total.

# Alumno: Nahuel Osvaldo Romano

cantidad = 5
precio_barbijo_caro = 0
maximo_cantidad_unidades = 0
cantidad_unidades_totales_jabon = 0
cantidad_barbijo_caro = 0
fabricante_barbijo_caro = 0


cantidad_barbijos = 0
cantidad_jabon = 0
cantidad_alcohol = 0

for cantidads in range (cantidad):

    tipo_producto = input("Ingrese el tipo de producto \n- barbijo \n- jabon\n- alcohol \n: ")

    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
        mensaje = "El producto ingresado no es valido, ingrese nuevamente"
        print(mensaje)
        tipo_producto = input("Ingrese nuevamente el tipo de producto \n- barbijo \n- jabon\n- alcohol \n: ")

    precio_producto = int(input("Ingrese el precio del producto entre 100 y 300: "))

    while precio_producto < 100 or precio_producto > 300:
        mensaje = "El precio del producto no puede ser menor a 100 o mayor a 300, ingrese nuevamente"
        print(mensaje)
        precio_producto = int(input("Ingrese nuevamente el precio del producto entre 100 y 300: "))

    cantidad_unidades = int(input("Ingrese la cantidad de unidaeds del producto: "))

    while cantidad_unidades <= 0 or cantidad_unidades > 1000:
        mensaje = "Las unidades no pueden ser menor a 0 y no pueden superar las 1000"
        print(mensaje)
        cantidad_unidades = int(input("Ingrese nuevamente la cantidad de unidades del producto: "))

    marca_producto = input("Ingrese la marca del producto: ")

    match tipo_producto:
        case "barbijo":
            if precio_producto > precio_barbijo_caro:
                precio_barbijo_caro = precio_producto
                cantidad_barbijo_caro = cantidad_unidades
                fabricante_barbijo_caro = marca_producto
        case "jabon":
            cantidad_unidades_totales_jabon += cantidad_unidades

if cantidad_unidades > maximo_cantidad_unidades:
    maximo_cantidad_unidades = cantidad_unidades
    nombre_fabricante_maximo = marca_producto

mensaje = f"""El barbijo más caro es: {precio_barbijo_caro} y su cantidad es: {cantidad_barbijo_caro}, fabricante: {fabricante_barbijo_caro}
              Del ingreso con más unidades el fabricante es: {nombre_fabricante_maximo}
              Unidad de jabones en total: {cantidad_unidades_totales_jabon}"""

print(mensaje)