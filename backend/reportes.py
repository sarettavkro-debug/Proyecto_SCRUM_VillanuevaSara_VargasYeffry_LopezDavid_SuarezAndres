# Responsable: Desarrollador 4 – Development Team & Scrum Master
from modelos import clientes, servicios, matriculas

def listar_clientes_inscritos(clientes):
    """
    Muestra en consola el listado completo de clientes registrados en el sistema.
    """
    print("\n" + "="*50)
    print("      REPORTE: CLIENTES INSCRITOS")
    print("="*50)
    
    if not clientes:
        print("No hay clientes registrados en el sistema.")
        return

    for id_cliente, datos in clientes.items():
        nombre = datos.get("nombre", "N/A")
        apellido = datos.get("apellido", "N/A")
        telefono = datos.get("telefono", "N/A")
        riesgo = datos.get("nivel_riesgo", "N/A")
        print(f"• ID: {id_cliente} | Nombre: {nombre} {apellido} | Tel: {telefono} | Riesgo: {riesgo}")
    
    print("-" * 50)

def listar_servicios_y_capacidad():
    """
    Descripción: Imprime los servicios offered junto con sus cupos ocupados vs la capacidad máxima.
    Dev4: Implementar recorrido e impresión formateada de 'servicios'.
    """
    pass

def listar_clientes_riesgo_alto():
    """
    Descripción: Filtra e imprime únicamente los clientes cuya etiqueta de riesgo sea 'alto'.
    Dev4: Implementar filtro sobre la lista 'clientes'.
    """
    pass

def mostrar_progreso_clientes():
    """
    Descripción: Despliega la asistencia y el avance físico guardado en las matrículas.
    Dev4: Implementar recorrido de la lista 'matriculas'.
    """
    pass