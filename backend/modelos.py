# Responsable: Desarrollador 1 – Development Team

# Listas globales (Base de datos en memoria del gimnasio)
clientes = []
servicios = []
matriculas = []

def crear_cliente(id_num, nombres, apellidos, direccion, celular, fijo, estado="En proceso de inscripción", riesgo="medio"):
    """
    Descripción: Recibe los datos personales de un cliente y retorna un diccionario
    con la estructura estándar.
    Dev1: Implementar el retorno del diccionario con sus campos.
    """
    return{
        "id_num": id_num,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "celular": celular,
        "fijo": fijo,
        "estado": estado,
        "riesgo": riesgo
    }

def crear_servicio(id_servicio, nombre, capacidad):
    return {
        "id_servicio": id_servicio,
        "nombre": nombre,
        "capacidad_maxima": capacidad,
        "cupos_ocupados": 0
    }