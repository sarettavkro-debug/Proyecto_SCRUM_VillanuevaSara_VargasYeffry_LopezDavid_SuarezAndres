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
    
    for c in clientes:
        if str(c["id_num"]).strip() == id_num:
            print("Ya existe un cliente registrado con ese ID.")
            return

    riesgo = input("Riesgo (bajo/medio/alto): ").strip().lower()
    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    direccion = input("Dirección: ").strip()
    celular = input("Celular: ").strip()
    
    nuevo_cliente = crear_cliente(
    id_num, 
    nombres, 
    apellidos, 
    direccion, 
    celular, 
    fijo="", 
    riesgo=riesgo 
    )
    clientes.append(nuevo_cliente)
    
    print(f"Cliente {nombres} {apellidos} registrado completamente.")

import modelos

def cargar_servicios_iniciales():
    """Carga los servicios base garantizando que la lista se llene."""
    modelos.servicios.clear()  # Limpia la lista por si tenía basura
    modelos.servicios.extend([
        modelos.crear_servicio("1", "Yoga", 15),
        modelos.crear_servicio("2", "Pilates", 12),
        modelos.crear_servicio("3", "Entrenamiento personalizado", 5),
        modelos.crear_servicio("4", "Piscina", 20),
        modelos.crear_servicio("5", "Gimnasio general", 30)
    ])