from Package_Funciones.funciones import *

lista_empleados = []
identidad = 1
contador = 0

while True:
    mostrar_menu("principal")
    
    opcion = opciones_menu("numeros")

    match opcion:
        case 1:
            if contador == 0:
                leer_csv_json(lista_empleados)
                contador += 1
            else:
                print("[ERROR] NO PUEDE VOLVER A CARGAR DATOS")
        case 2:
            usuario = crear_usuario()
            dar_de_alta(lista_empleados, usuario, identidad)
            identidad += 1
        case 3:
            id_persona = input("Ingrese el id: ")
            while not validar_id(id_persona):
                id_persona = input("Ingrese nuevamente el id: ")
            print(modificar(lista_empleados, int(id_persona)))
        case 4:
            id_persona = input("Ingrese el id: ")
            while not validar_id(id_persona):
                id_persona = input("Ingrese nuevamente el id: ")
            print(eliminar(lista_empleados, int(id_persona)))
        case 5:
            mostrar_empleados_p_s_a(lista_empleados)
        case 6:
            empleados_analistas(lista_empleados)
        case 7:
            print(salario_promedio(lista_empleados))
        case 8:
            ordenar_empleados(lista_empleados)
        case 9:
            mostrar_empleados(lista_empleados, "empleados", "True")
        case 10:
            print("ADIOS!")
            break 
        case 11:
            mostrar_empleados(lista_empleados, "empleados", "False")
        case _:
            print("REINTENTAR")