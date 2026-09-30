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
    while nombres =="" or not nombres.replace(" ","").isalpha():
        print("Los nombres deben contener solo letras y no pueden estar vacios. ")
        return

    apellidos = input("Apellidos: ").strip()
    while apellidos=="" or not apellidos.replace(" ","").isalpha():
        print("Los apellidos deben contener solo letras y no pueden estar avcios. ")
        return

    direccion = input("Direccion: ").strip()

    if direccion == "":
        print("La direccion no puede estar vacia. ")
        return

    celular = input("Celular: ")

    while True:
        celular = input("Celular: ").strip()
        try:
            int(celular)
            break
        except ValueError:
            print("El celular solo debe contener numero y no puede estar vacio. ")

    tel_fijo = input("Telefono_fijo: ").strip()

    while True:
        tel_fijo = input("Telefono fijo: ").strip()
        try:
            int(tel_fijo)
            break
        except ValueError:
            print("El telefono fijp debe contener solo numeros y no puede estar vacio. ")

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