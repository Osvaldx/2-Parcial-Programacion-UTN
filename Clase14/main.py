from Package_Funciones.funciones import *

lista_empleados = []
identidad = 1

while True:
    mostrar_menu("principal")
    
    opcion = opciones_menu()

    match opcion:
        case 1:
            usuario = crear_usuario()
            dar_de_alta(lista_empleados, usuario, identidad)
            identidad += 1
        case 2:
            id_persona = input("Ingrese el id: ")
            while not validar_id(id_persona):
                id_persona = input("Ingrese nuevamente el id: ")
            print(modificar(lista_empleados, int(id_persona)))
        case 3:
            id_persona = input("Ingrese el id: ")
            while not validar_id(id_persona):
                id_persona = input("Ingrese nuevamente el id: ")
            eliminar(lista_empleados, int(id_persona))
        case 4:
            mostrar_empleados(lista_empleados)
        case 5:
            mostrar_gerentes(lista_empleados)
        case 6:
            print(salario_promedio(lista_empleados))
        case 7:
            print("Adios!")
            break
        case _:
            print("REINTENTAR")