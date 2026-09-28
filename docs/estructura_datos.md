Responsable: Desarrollador 1 – Development Team
# Estructura de Datos (Diccionarios)

- Dev 1: Documentar aquí los campos y tipos de datos del diccionario Cliente y Servicio.

En este documento se realiza una descripción de la estructura de datos utilizada por el sistema de gestión de Gimnasio ForceTech, detallando los campos, tipos de datos, las restricciones y los valores permitidos por las entidades "Cliente" y "Servicio".

## Diccionario de datos: Cliente
Entidad que representa a las personas inscritas en el gimnasio, sus datos de contacto y datos dentro del sistema.

Aquí irá el campo, tipo de dato, descripción, restricciones y notas.

- `id_num`(Cadena de texto / VARCHAR 20): Número de identificación oficial del cliente (Cédula, DNI, etc). Único, no nulo.
- `nombres`(Cadena de texto / VARCHAR 50): Nombre(s) del cliente. No nulo.
- `apellidos`(Cadena de texto / VARCHAR 50): Apellido(s) del cliente. No nulo.
- `direccion`(Cadena de texto / VARCHAR 150): Dirección de residencia del cliente. Opcional según las reglas de negocio.
- `celular`(Cadena de texto / VARCHAR 15): Número de teléfono celular de contacto. Formato numérico validado.
- `fijo`(Cadena de texto / VARCHAR 15): Número de teléfono fijo de contacto. Opcional.
- `estado`(Enumerado / ENUM): Estado actual del cliente dentro del proceso de inscripción. Valor por defecto: "En proceso de inscripción".
- `riesgo`(Enumerado / ENUM): Nivel de riesgo asociado a la condición física/salud del cliente. Valor por defecto: "medio".

## Estados del Cliente
- En proceso de inscripción: El cliente inició el registro pero aún no ha completado todos los requisitos.
- Inscrito: El cliente completó su suscripción pero aún no ha sido asignado o no ha iniciado una actividad.
- Activo: El cliente participa en uno o más servicios del gimnasio.
- Inactivo: El cliente no tiene actividad actual (pausa, retiro temporal o definitivo).

## Diccionario de datos: Servicio
Entidad que representa los distintos ofrecidos por el gimnasio (clases, entrenamientos y accesos).

- `id_servicio`(Cadena de texto / VARCHAR 20): Identificador único del servicio. No nulo.
- `nombre`(Cadena de texto / VARCHAR 50): Nombre del servicio ofrecido. No nulo.
- `capacidad_maxima`(Entero / INT): Número máximo de clientes que pueden asignarse simultáneamente al servicio. No nulo. Debe ser mayor a 0.
- `cupos_ocupados`(Entero / INT): Número de cupos actualmente ocupados. Inicializado en 0.

