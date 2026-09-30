# Responsable: Desarrollador 2 – Development Team
from modelos import clientes, servicios, crear_cliente, crear_servicio

def registrar_cliente():
    """
    Descripción: Solicita por consola los datos personales del cliente, invoca a
    crear_cliente() para armar la estructura y lo guarda en la lista global 'clientes'.
    Dev2: Implementar lectura por consola (input) y guardado en lista.
    """
    print("===== REGISTRAR CLIENTE =====")

    id_num = input("ID: ").strip()
    if id_num == "":
        print("El ID no puede estar vacio. ")
        return

    for c in clientes:
        if c ["id_num"] == id_num:
            print("Ya existe un cliente con ese ID.")
            return

    riesgo = input("Riesgo (bajo/medio/alto): ").strip().lower()
    while riesgo not in ("bajo", "medio", "alto"):
        print("Valor invalido. Intenta escribiendo bajo, medio o alto. Intenta de nuevo bro.")
        riesgo = input("Riesgo (bajo/medio/alto): ").strip().lower()

    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()

    if nombres == "" or apellidos == "":
        print("Los nombres y apellidos son obligatorios. Intenta de nuevo.")
        return
    
    direccion = input("Direccion: ").strip()

    if direccion == "":
        print("La direccion no puede estar vacia. ")
        return
    
    celular = input("Celular: ")

    if celular=="":
        print ("El celular no puede estar vacio y solo puede contener numeros. ")

    tel_fijo = input("Telefono_fijo: ").strip()

    if tel_fijo=="":
        print("El telefono fijo debe contener solo numeros")

    cliente = crear_cliente(id_num, nombres, apellidos, direccion, celular, tel_fijo, riesgo=riesgo)
    clientes.append(cliente)
    print(f"Cliente {nombres} {apellidos} registrado completamente. ")


def cargar_servicios_iniciales():
    """
    Descripción: Carga los 5 servicios base exigidos por el gimnasio (Yoga, Pilates,
    Entrenamiento personalizado, Piscina, Gimnasio general) dentro de la lista 'servicios'.
    Dev2: Implementar la precarga de datos al iniciar la aplicación.
    """

    if len(servicios) > 0:
        return
    
    servicios.append(crear_servicio(1, "Yoga", 15))
    servicios.append(crear_servicio(2, "Pilates", 12))
    servicios.append(crear_servicio(3, "Entrenamiento personalizado", 5))
    servicios.append(crear_servicio(4, "Piscina", 20))
    servicios.append(crear_servicio(5, "Gimnasio general", 30))