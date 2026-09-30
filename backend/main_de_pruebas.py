from inscripciones import registrar_cliente, cargar_servicios_iniciales

servicios = cargar_servicios_iniciales()
print("Servicio cargado: ", servicios)

cliente_prueba = registrar_cliente()
print("Cliente registrado: ", cliente_prueba)