# Responsable: Desarrollador 3 – Development Team
from modelos import clientes, servicios, matriculas

def matricular_cliente():

    try:
        idC = int(input("ingrese el id del cliente: "))
    except ValueError:
        print("el id debe ser un numero entero")
        return

    cliente_encontrado=None
    for cliente in clientes:
        if cliente.get("id_num") == idC:
            cliente_encontrado=cliente

    if not cliente_encontrado:
        print("no se encontro un cliente ")
        return

    if not servicios:
        print("no se encontraron servicios")
        return



    print("Servicios Disponibles")
    for s in servicios:
        print(f"ID: {s.get('id_servicio')} | Nombre: {s.get('nombre')} | Cupos: {s.get('cupos_ocupados')}/{s.get('capacidad_maxima')}")

    try:
        idS = int(input("ingrese el id del servicio que quiere matricular "))
    except ValueError:
        print("el id tiene que ser un numero entero")
        return

    servicio_encontrado=None  
    for s in servicios:  
        if s.get("id_servicio")==idS:
            servicio_encontrado=s
            break
    if not servicio_encontrado:
        print("no se encontro el servicio ")
        return
    if servicio_encontrado["cupos_ocupados"] >= servicio_encontrado["capacidad_maxima"]:
        print("no hay cupos para este servicio")
        return

    servicio_encontrado["cupos_ocupados"] += 1

    nueva_matricula = {
        "id_cliente": idC,
        "id_servicio": idS,
        "asistencia": [],
        "evaluaciones_fisicas": []
    }
    
    matriculas.append(nueva_matricula)
    print("¡Matrícula registrada con éxito!")

    """
    Descripción: Solicita el ID de un cliente, valida que exista, muestra los servicios
    disponibles y verifica que cupos_ocupados < capacidad_maxima antes de registrar la matrícula.
    Dev3: Implementar la búsqueda de clientes, validación de aforo y registro en 'matriculas'.
    """
    

def registrar_asistencia_y_progreso():

    try:    
        idC=int(input("ingrese el id del cliente: "))
    except ValueError:
        print("el id debe ser un numero entero")
        return
    matriculas_cliente =[m for m in matriculas if m.get("id_cliente") == idC]

    if not matriculas_cliente:
        print("el cliente no tiene matriculas registradas ")
        return

    print("Opciones de registro:")
    print("1.Registrar asistencia")
    print("2.Registrar evaluación física")
    opcion=input("selecione una de las opciones ")
    if opcion =="1":
        fecha=input("ingrese la fecha de asistencia (DD/MM/AAAA)")
        for m in matriculas_cliente:
            m["asistencia"].append(fecha)
            print("asistencia registrada")

    elif opcion =="2":
        peso =input("ingrese su peso actual en kg: ")
        observaciones=input("ingrese las observaciones fisicas: ")
        evaluacion = {"peso":peso,"observaciones":observaciones}

        for m in matriculas_cliente:
            m["evaluaciones_fisicas"].append(evaluacion)
            print("evaluacio fisica registrada")

    else:
        print("opcion no valida")
    """
    Descripción: Permite al instructor registrar la asistencia y las evaluaciones físicas
    periódicas de un cliente matriculado.
    Dev3: Implementar la actualización de datos sobre el diccionario de matrículas.
    """
    