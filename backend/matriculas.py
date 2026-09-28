# Responsable: Desarrollador 3 – Development Team
from modelos import clientes, servicios, matriculas

def matricular_cliente():
   
    try:
        idC = int(input("Ingrese el ID del cliente: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    cliente_encontrado = None
    for cliente in clientes:
        if cliente.get("id_num") == idC:
            cliente_encontrado = cliente
            break

    if not cliente_encontrado:
        print("No se encontró el cliente.")
        return

    if not servicios:
        print("No hay servicios registrados en el sistema.")
        return

    print("\n--- Servicios Disponibles ---")
    for s in servicios:
        print(f"ID: {s.get('id_servicio')} | Nombre: {s.get('nombre')} | Cupos: {s.get('cupos_ocupados')}/{s.get('capacidad_maxima')}")

    try:
        idS = int(input("\nIngrese el ID del servicio a matricular: "))
    except ValueError:
        print("El ID del servicio debe ser un número entero.")
        return

    servicio_encontrado = None
    for s in servicios:
        if s.get("id_servicio") == idS:
            servicio_encontrado = s
            break

    if not servicio_encontrado:
        print("No se encontró el servicio.")
        return

    if servicio_encontrado["cupos_ocupados"] >= servicio_encontrado["capacidad_maxima"]:
        print("No hay cupos disponibles (aforo máximo alcanzado).")
        return

    fecha_inicio = input("Ingrese la fecha de inicio (ej. YYYY-MM-DD): ")
    duracion = input("Ingrese la duración (ej. 1 mes, 3 meses): ")
    instructor = input("Ingrese el nombre del instructor asignado: ")

    servicio_encontrado["cupos_ocupados"] += 1

    nueva_matricula = {
        "id_cliente": idC,
        "id_servicio": idS,
        "fecha_inicio": fecha_inicio,
        "duracion": duracion,
        "instructor": instructor,
        "asistencia": [],
        "evaluaciones_fisicas": []
    }

    matriculas.append(nueva_matricula)
    print("\n¡Matrícula registrada exitosamente!")

    

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

