Responsable: Desarrollador 1 – Development Team
# Estructura de Datos (Diccionarios)

- Dev 1: Documentar aquí los campos y tipos de datos del diccionario Cliente y Servicio.

En este documento se realiza una descripción de la estructura de datos utilizada por el sistema de gestión de Gimnasio ForceTech, detallando los campos, tipos de datos, las restricciones y los valores permitidos por las entidades "Cliente" y "Servicio".

## Diccionario de datos: Cliente
Entidad que representa a las personas inscritas en el gimnasio, sus datos de contacto y datos dentro del sistema.

Aquí irá el campo, tipo de dato, descripción, restricciones y notas.

- `id_num`: Número de identificación oficial del cliente (Cédula, DNI, etc). Único, no nulo.
- `nombres`: Nombre(s) del cliente. No nulo.
- `apellidos`: Apellido(s) del cliente. No nulo.
- `direccion`: Dirección de residencia del cliente. Opcional según las reglas de negocio.
- `celular`: Número de teléfono celular de contacto. Formato numérico validado.
- `fijo`: Número de teléfono fijo de contacto. Opcional.
- `estado`: Estado actual del cliente dentro del proceso de inscripción. Valor por defecto: "En proceso de inscripción".
- `riesgo`: Nivel de riesgo asociado a la condición física/salud del cliente. Valor por defecto: "medio".