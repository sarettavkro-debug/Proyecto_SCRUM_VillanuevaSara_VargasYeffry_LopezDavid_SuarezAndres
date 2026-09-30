Responsable: Desarrollador 4 – Scrum Master
# Plan de Pruebas Manuales

# Plan de Casos de Prueba - Sistema ForceTech

Este documento contiene la matriz de casos de prueba (CP01 a CP08) para validar las reglas de negocio, la integridad de los datos y la correcta ejecución de los módulos del sistema ForceTech.

| Código | Módulo | Descripción / Escenario | Datos de Entrada | Resultado Esperado | Criterio de Aprobación |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CP01** | Entorno Base | Inicialización correcta de la estructura de diccionarios en memoria | Ejecución de `main.py` | Diccionarios vacíos o con datos iniciales cargados sin arrojar excepciones de Python | **Aprobado** si no hay errores al iniciar el programa. |
| **CP02** | Inscripciones | Registro exitoso de un nuevo cliente con datos válidos | ID: `101`, Nombre: `Sara`, Teléfono: `3001234567`, Riesgo: `Bajo` | Cliente guardado correctamente en la memoria con un mensaje de confirmación | **Aprobado** si el cliente se almacena en el diccionario de clientes. |
| **CP03** | Inscripciones | Intento de registro de cliente con ID duplicado | ID: `101` (ya existente en el sistema) | Mensaje de error indicando que el ID ya se encuentra registrado | **Aprobado** si el sistema impide la duplicación del documento. |
| **CP04** | Matrículas | Matrícula exitosa de cliente en disciplina con aforo disponible | ID Cliente: `101`, Servicio: `Yoga` (aforo > 0) | Matrícula registrada, cupos disponibles reducidos en `1` | **Aprobado** si el cupo disminuye y la relación cliente-servicio se guarda. |
| **CP05** | Matrículas | Intento de matrícula en servicio sin cupos disponibles (Aforo lleno) | ID Cliente: `101`, Servicio: `Piscina` (cupos libres = 0) | Alerta en consola indicando que el aforo está completo | **Aprobado** si se deniega la inscripción a clases sin cupo. |
| **CP06** | Reportes | Generación del informe de clientes inscritos y aforo general | Selección de opción `Reportes` en menú | Despliegue ordenado de la lista de clientes y estado de cupos por disciplina | **Aprobado** si imprime la totalidad de datos en formato legible. |
| **CP07** | Reportes | Filtrado de clientes clasificados con nivel de riesgo "Alto" | Ejecución de `listar_clientes_riesgo_alto()` | Despliegue exclusivo de los clientes cuyo campo `nivel_riesgo` sea "Alto" | **Aprobado** si omite clientes con riesgo medio o bajo. |
| **CP08** | Integración | Manejo de entradas inválidas del usuario en el menú principal | Selección de opción inexistente (ej. `99` o letras) | Mensaje de advertencia "Opción no válida" sin que el programa se cierre inesperadamente | **Aprobado** si la consola mantiene el flujo activo tras el error. |