# Responsable: Desarrollador 2 – Development Team
from inscripciones import registrar_cliente, cargar_servicios_iniciales
from matriculas import matricular_cliente, registrar_asistencia_y_progreso
from reportes import (
    listar_clientes_inscritos,
    listar_servicios_y_capacidad,
    listar_clientes_riesgo_alto,
    mostrar_progreso_clientes
)

def menu_principal():
    """
    Descripción: Despliega el menú interactivo con ciclo 'while' e 'if/elif/else'
    para orquestar las llamadas a cada módulo del programa.
    Dev2: Implementar la lógica del menú y la captura de opciones del usuario.
    """
    cargar_servicios_iniciales()

    while True:
        print("======= MENU PRINCIPAL =======")
        print("1. Registrar cliente. ")
        print("2. Matricular cliente. ")
        print("3. Registrar asistencia y progreso. ")
        print("4. Listar clientes inscritos. ")
        print("5. Listar servicios y capacidad. ")
        print("6. listar clientes con bajo rendimiento o riesgo. ")
        print("7. Mostrar el progreso de los clientes. ")
        print("8. Salir....")

        opcion = input("Seleccionar una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            matricular_cliente()
        elif opcion == "3":
            registrar_asistencia_y_progreso()
        elif opcion == "4":
            listar_clientes_inscritos()
        elif opcion == "5": 
            listar_servicios_y_capacidad()
        elif opcion == "6":
            listar_clientes_riesgo_alto()
        elif opcion == "7":
            mostrar_progreso_clientes()
        elif opcion == "8":
            print("Saliendo del programa....")
            break
        else:
            print("Opcion invaldia, intenta de nuevo. ")

if __name__ == "__main__":
    menu_principal()