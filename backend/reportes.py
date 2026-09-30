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

def listar_servicios_y_capacidad(servicios):
    """
    Muestra la lista de servicios/disciplinas con sus cupos máximos y disponibles.
    """
    print("\n" + "="*50)
    print("      REPORTE: SERVICIOS Y CAPACIDAD DE AFORO")
    print("="*50)
    
    if not servicios:
        print("No hay servicios cargados en el sistema.")
        return

    for id_servicio, datos in servicios.items():
        nombre = datos.get("nombre", "N/A")
        aforo_max = datos.get("aforo_maximo", 0)
        cupos_disp = datos.get("cupos_disponibles", 0)
        matriculados = aforo_max - cupos_disp
        
        print(f"• {nombre} (ID: {id_servicio})")
        print(f"  - Capacidad Máxima: {aforo_max} personas")
        print(f"  - Matriculados: {matriculados} | Cupos Libres: {cupos_disp}")
    
    print("-" * 50)

def listar_clientes_riesgo_alto(clientes):
    """
    Filtra y muestra únicamente a los clientes clasificados con nivel de riesgo 'Alto'.
    """
    print("\n" + "="*50)
    print("      REPORTE: CLIENTES DE ALTO RIESGO")
    print("="*50)
    
    if not clientes:
        print("No hay clientes registrados en el sistema.")
        return

    encontrados = False
    for id_cliente, datos in clientes.items():
        nivel_riesgo = str(datos.get("nivel_riesgo", "")).strip().capitalize()
        if nivel_riesgo == "Alto":
            encontrados = True
            nombre = datos.get("nombre", "N/A")
            apellido = datos.get("apellido", "N/A")
            telefono = datos.get("telefono", "N/A")
            print(f"⚠️ ID: {id_cliente} | Nombre: {nombre} {apellido} | Tel: {telefono}")

    if not encontrados:
        print("No se encontraron clientes registrados con nivel de riesgo 'Alto'.")
        
    print("-" * 50)

def mostrar_progreso_clientes():
    """
    Descripción: Despliega la asistencia y el avance físico guardado en las matrículas.
    Dev4: Implementar recorrido de la lista 'matriculas'.
    """ 
    pass