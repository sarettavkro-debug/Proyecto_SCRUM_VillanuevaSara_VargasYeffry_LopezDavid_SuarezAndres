# Responsable: Desarrollador 4 – Development Team & Scrum Master
from modelos import clientes, servicios, matriculas

from modelos import clientes

def listar_clientes_inscritos(clientes=clientes):
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    print("\n=== LISTA DE CLIENTES INSCRITOS ===")
    for c in clientes:
        print(f"ID: {c['id_num']} | Nombre: {c['nombres']} {c['apellidos']} | Riesgo: {c['riesgo']}")
        
    print("-" * 50)

def listar_servicios_y_capacidad(servicios):
    print("\n" + "=" * 50)
    print("      REPORTE: SERVICIOS Y CAPACIDAD DE AFORO")
    print("=" * 50)

    if not servicios:
        print("No hay servicios cargados en el sistema.")
        return

    for s in servicios:
        id_servicio = s.get("id_servicio", "N/A")
        nombre = s.get("nombre", "N/A")
        aforo_max = s.get("capacidad_maxima", 0)
        cupos_ocupados = s.get("cupos_ocupados", 0)
        cupos_libres = max(0, aforo_max - cupos_ocupados)

        print(f"• {nombre} (ID: {id_servicio})")
        print(f"  - Capacidad Máxima: {aforo_max} personas")
        print(f"  - Matriculados: {cupos_ocupados} | Cupos Libres: {cupos_libres}")
        print("-" * 50)

def listar_clientes_riesgo_alto(clientes):
    print("\n" + "=" * 50)
    print("      REPORTE: CLIENTES DE ALTO RIESGO")
    print("=" * 50)

    if not clientes:
        print("No hay clientes registrados en el sistema.")
        return

    encontrados = False
    for cliente in clientes:
        # Extrae el valor del riesgo asegurando convertirlo a texto en minúsculas
        riesgo = str(cliente.get("riesgo", cliente.get("nivel_riesgo", ""))).lower().strip()
        
        if riesgo in ["alto", "high", "true"]:
            encontrados = True
            id_num = cliente.get("id_num", cliente.get("id_cliente", "N/A"))
            nombres = cliente.get("nombres", cliente.get("nombre", "N/A"))
            apellidos = cliente.get("apellidos", "")
            
            print(f"• ID: {id_num} | Cliente: {nombres} {apellidos}")
            print(f"  - Nivel de Riesgo: {riesgo.capitalize()}")
            print("-" * 50)

    if not encontrados:
        print("No se encontraron clientes con alto riesgo.")
    print("-" * 50)

def mostrar_progreso_clientes(matriculas):
    print("\n" + "=" * 50)
    print("      REPORTE: PROGRESO Y SERVICIOS POR CLIENTE")
    print("=" * 50)

    if not matriculas:
        print("No hay matrículas ni progreso registrado en el sistema.")
        return

    for m in matriculas:
        id_cliente = m.get("id_cliente", m.get("id_num", "N/A"))
        servicio = m.get("servicio", m.get("nombre_servicio", "N/A"))
        progreso = m.get("progreso", m.get("asistencia", "0%"))
        
        print(f"• Cliente ID: {id_cliente}")
        print(f"  - Servicio: {servicio}")
        print(f"  - Progreso/Asistencia: {progreso}")
        print("-" * 50)
    print("-" * 50)