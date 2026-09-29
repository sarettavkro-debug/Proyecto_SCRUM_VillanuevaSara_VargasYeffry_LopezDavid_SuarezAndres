Responsable: Desarrollador 4 – Scrum Master
# PROYECTO: Sistema de Gestión - Gimnasio ForceTech

**Integrantes:**
* Juan Andrés Suárez (Dev 1)
* Yeffry Vargas (Dev 2)
* David López (Dev 3)
* Sara Villanueva Caro (Dev 4)
**Asignatura:** Scrum y Metodologías ágiles  
**Institución:** Campuslands  
**Fecha:** Septiembre de 2026  

---

## 1. SITUACIÓN PROBLEMA

El Gimnasio ForceTech enfrenta actualmente la necesidad de optimizar y centralizar el seguimiento y control de sus clientes y servicios ofrecidos. La falta de un sistema automatizado dificulta la captura precisa de datos personales, la clasificación de niveles de riesgo físico de los usuarios, el control estricto del aforo máximo en disciplinas (como Yoga, Pilates, Piscina, Gimnasio general y Entrenamiento personalizado) y la generación oportuna de reportes operativos.

Para dar solución a esta problemática, el equipo de desarrollo implementa una aplicación en Python bajo el marco de trabajo ágil SCRUM. Esta solución permite gestionar inscripciones, controlar cupos en tiempo real, asignar instructores y evaluar periódicamente el progreso físico de los clientes con los más altos estándares de calidad.

---

## 2. MARCO DE TRABAJO SCRUM

### 2.1 Roles del Equipo
* **Product Owner:** Define y prioriza los requisitos del Gimnasio ForceTech en el Product Backlog.
* **Scrum Master (Dev 4):** Facilita el proceso SCRUM, remueve bloqueos técnicos y administra el tablero del proyecto.
* **Development Team (Dev 1, Dev 2, Dev 3, Dev 4):** Encargados de la arquitectura, diseño de modelos, programación de módulos y ejecuciones de prueba.

### 2.2 Eventos
* **Sprint Planning:** Definición del alcance e historias de usuario seleccionadas para cada Sprint.
* **Daily Stand-up:** Reuniones diarias de 10 minutos para revisar avances en el tablero Kanban y coordinar integraciones.
* **Sprint Review & Retrospective:** Demostración del incremento funcional e identificación de mejoras para la siguiente iteración.

### 2.3 Seguimiento Diario (Daily Stand-ups)

#### 📌 Día 1: Configuración y Arquitectura Base
* **Fecha:** 26 de septiembre de 2026
* **Moderador:** Scrum Master (Dev 4)
* **Resumen de intervenciones:**
  * **Dev 1 & Dev 2:** Configuraron la estructura de carpetas, el archivo `backend/modelos.py` y el menú inicial en `main.py`.
  * **Dev 3:** Revisó la estructura de datos base para los módulos posteriores.
  * **Dev 4:** Creó y configuró el tablero Kanban en GitHub Projects, definiendo columnas, vistas, etiquetas y campos de Sprint.
* **Bloqueos / Impedimentos:** Ninguno.
* **Estado del Tablero:** Tarjeta #1 completada y movida a *Hecho*. Tarjetas del Sprint 1 asignadas.

#### 📌 Día 2: Módulo de Usuarios, Servicios y Requerimientos
* **Fecha:** 27 de septiembre de 2026
* **Moderador:** Scrum Master (Dev 4)
* **Plan de trabajo y compromisos del día:**
  * **Dev 1:** Redactará la especificación detallada de los diccionarios en `docs/estructura_datos.md`.
  * **Dev 2:** Implementará `registrar_cliente()` y `cargar_servicios_iniciales()` en `backend/inscripciones.py`.
  * **Dev 3:** Validará la compatibilidad de la estructura de diccionarios para el control de aforos en matrículas.
  * **Dev 4 (Scrum Master):** Redactará los Requerimientos Funcionales (RF) y No Funcionales (RNF) en `docs/documentacion.md` y supervisará las tarjetas del Sprint 1.
* **Bloqueos / Impedimentos reportados:** Ninguno.
* **Estado del Tablero:** Tarjeta #2 movida a *En curso*; Tarjeta #5 actualizada con la sección de Requerimientos.

#### 📌 Día 3: Módulo de Matrículas y Control de Aforo
* **Fecha:** 28 de septiembre de 2026
* **Moderador:** Scrum Master (Dev 4)
* **Plan de trabajo y compromisos del día:**
  * **Dev 1:** Apoyará en las pruebas de integración entre los módulos de inscripciones y matrículas en consola.
  * **Dev 2:** Finalizará la revisión del Pull Request para el módulo de inscripciones (`backend/inscripciones.py`) e integrará cambios a `main`.
  * **Dev 3:** Programará en `backend/matriculas.py` la lógica de matrículas validando el control de aforo y cupos máximos por servicio.
  * **Dev 4 (Scrum Master):** Actualizará la bitácora del proyecto, registrará capturas del estado del tablero y verificará el avance del Sprint 1.
* **Bloqueos / Impedimentos reportados:** Ninguno.
* **Estado del Tablero:** Tarjeta #2 movida a *En Revisión* / *Hecho*; Tarjeta #3 movida a *En Curso*.

---

## 3. LEVANTAMIENTO DE REQUERIMIENTOS

### 3.1 Requerimientos Funcionales (RF)
* **RF01 - Gestión de Clientes:** El sistema debe permitir registrar clientes con su ID, nombres, apellidos, dirección, teléfonos de contacto, estado y nivel de riesgo (Alto, Medio, Bajo).
* **RF02 - Catálogo de Servicios:** El sistema debe permitir consultar y gestionar los 5 servicios ofrecidos y su capacidad máxima.
* **RF03 - Módulo de Matrículas:** El sistema debe permitir matricular clientes en un servicio verificando que no se supere la capacidad máxima (aforo).
* **RF04 - Módulo de Reportes:** El sistema debe generar reportes consolidando clientes inscritos, servicios activos, aforo ocupado y usuarios con riesgo alto.

### 3.2 Requerimientos No Funcionales (RNF)
* **RNF01 - Usabilidad:** Interfaz de consola clara e intuitiva estructurada mediante menús numéricos.
* **RNF02 - Mantenibilidad:** Código modularizado en archivos independientes (`modelos.py`, `inscripciones.py`, `matriculas.py`, `reportes.py`).
* **RNF03 - Integridad de Datos:** Validación de tipos de datos y control de redundancia en la memoria del sistema.

---

## 4. METODOLOGÍA SCRUM Y ROLES

El desarrollo de la aplicación para el Gimnasio ForceTech se gestiona mediante la metodología ágil **SCRUM**, organizada en un ciclo de desarrollo de 5 días con 2 Sprints operativos.

### 4.1 Definición de Roles
* **Product Owner:** Encargado de priorizar el Product Backlog y definir los criterios de aceptación para las funcionalidades del gimnasio.
* **Scrum Master (Dev 4):** Lidera la gestión del tablero en GitHub Projects, facilita los Daily Stand-ups, remueve bloqueos técnicos y coordina la integración del equipo.
* **Equipo de Desarrollo (Dev 1, Dev 2, Dev 3, Dev 4):**
  * **Dev 1:** Arquitectura base y modelos (`backend/modelos.py`).
  * **Dev 2:** Módulo de inscripciones y registro de clientes (`backend/inscripciones.py`).
  * **Dev 3:** Módulo de matrículas y control de aforo (`backend/matriculas.py`).
  * **Dev 4:** Módulo de reportes (`backend/reportes.py`) y documentación oficial.

### 4.2 Artefactos y Eventos
* **Product Backlog:** Listado de las 6 User Stories/Tarjetas principales creadas en GitHub Projects.
* **Sprint Backlog:** Selección de tareas asignadas para la iteración actual.
* **Daily Stand-up:** Sincronización diaria de 10 minutos para revisar el estado del tablero Kanban.

---

## 5. EVIDENCIAS DEL TABLERO VIRTUAL

### 5.1 Estructura del Tablero Kanban (GitHub Projects)
El proyecto cuenta con un tablero Kanban configurado con 5 estados de flujo de trabajo:
1. **Reserva (Backlog):** Tareas pendientes para Sprints futuros.
2. **Por Hacer (Sprint Backlog):** Tareas priorizadas para el Sprint activo.
3. **En Curso (In Progress):** Tareas en desarrollo activo.
4. **En Revisión (In Review):** Tareas pendientes de verificación o Pull Request.
5. **Hecho (Done):** Tareas finalizadas y probadas.

### 5.2 Capturas y Estado del Tablero (Día 1)

![Captura](<../Imagenes/Kanban dia 1 actualizado.0.png>)

* **Organización por Sprints:**
  * **Sprint 1 (Días 1 a 3):** Enfocado en configuración, modelos de datos, inscripciones de clientes y matrículas con control de aforo.
  * **Sprint 2 (Días 4 y 5):** Enfocado en generación de reportes, pruebas cruzadas e integración final.
* **Metadatos asignados:** Cada tarjeta cuenta con sus respectivos responsables (*Assignees*), etiquetas de clasificación (`backend`, `documentation`, `setup`, `testing`) y la iteración asignada.

### 5.3 Evidencias del Tablero - Día 2

![Captura](<../Imagenes/Kanban día 2 actualizado.png>)

Al finalizar el Día 2, el tablero Kanban refleja el inicio de los trabajos de desarrollo técnico del Sprint 1:

* **Reserva (Backlog):** Se mantienen las tarjetas #4 (Reportes) y #6 (Integración final) asignadas para el Sprint 2.
* **Por hacer:** Tarjeta #3 (Módulo de Matrículas) lista para el Día 3.
* **En curso:** Tarjeta #2 (Módulo de Usuarios e Inscripciones) en desarrollo activo por Dev 2 y Dev 1. Tarjeta #5 (Documentación y Requerimientos por Dev 4).
* **Hecho:** Tarjeta #1 (Configuración de entorno).

### 5.4 Evidencias del Tablero - Día 3 (Módulo de Matrículas y Control de Aforo)

![Captura](<../Imagenes/Kanban día 3.png>)

Al finalizar el Día 3, el tablero en GitHub Projects evidencia el avance y la culminación del desarrollo técnico correspondiente al **Sprint 1**:

* **Reserva (Backlog):** Se mantienen aisladas las Tarjetas **#4** (Módulo de Reportes) y **#6** (Integración final y entrega), las cuales se activarán al inicio del Sprint 2 (Días 4 y 5).
* **Por hacer:** Columna despejada debido a que todas las historias del Sprint 1 han pasado a fase de ejecución o revisión.
* **En curso:** 
  * **Tarjeta #3 (Módulo de Matrículas y Control de Aforo):** Asignada a **Dev 3**, enfocada en la programación de la lógica en `backend/matriculas.py` para la validación de cupos máximos por disciplina.
* **En revisión:** 
  * **Tarjeta #2 (Módulo de Inscripciones y Clientes):** Asignada a **Dev 2**, en proceso de revisión de código y validación del Pull Request hacia la rama principal (`main`).
    * **Tarjeta #5:** Documentación técnica, Requerimientos (RF/RNF) y gestión del marco SCRUM por el Scrum Master (Dev 4).
* **Hecho:** 
  * **Tarjeta #1:** Configuración inicial del proyecto y entorno de trabajo.

## 6. Historias de Usuario y Criterios de Aceptación

A continuación se detallan las Historias de Usuario (HU) definidas para el desarrollo del sistema ForceTech, extraídas del Backlog del proyecto:

## Historia de Usuario 01

| Campo | Detalle |
|---|---|
| **Prioridad** | Alta |
| **Código del requerimiento** | RF01 |
| **Nombre del requerimiento** | Configuración de Entorno y Arquitectura Base |
| **Actor** | Desarrollador / Scrum Master |
| **Descripción** | Como desarrollador quiero configurar la estructura base del repositorio en GitHub y el entorno local para permitir el desarrollo colaborativo y modular del sistema ForceTech. |
| **Funcionalidad** | Establecer la arquitectura de archivos del proyecto, las ramas de Git (`main` y ramas por desarrollador) e inicializar las carpetas `backend/` y `docs/` con sus respectivos archivos borrador. |
| **Criterios de Aceptación** | 1. El sistema y repositorio deben contar con la rama principal `main` y ramas independientes configuradas por desarrollador.<br>2. El archivo `.gitignore` debe incluir las excepciones requeridas para proyectos en Python.<br>3. La estructura de carpetas debe reflejar la separación entre código fuente (`backend/`) y documentación (`docs/`). |
| **Restricciones** | Ningún desarrollador debe hacer commits directos a la rama `main` sin la aprobación previa de un Pull Request (PR) por parte de otro integrante. |

## Historia de Usuario 02

| Campo | Detalle |
|---|---|
| **Prioridad** | Alta |
| **Código del requerimiento** | RF03 |
| **Nombre del requerimiento** | Módulo de Matrículas y Control de Aforo |
| **Actor** | Administrador del Gimnasio |
| **Descripción** | Como administrador puedo matricular a un cliente previamente inscrito en una disciplina específica con el fin de controlar la asistencia y garantizar que no se supere el aforo máximo permitido. |
| **Funcionalidad** | Consultar la lista de disciplinas disponibles (Yoga, Pilates, Piscina, etc.), verificar la cantidad de cupos disponibles y asociar la matrícula del cliente disminuyendo en 1 la capacidad disponible. |
| **Criterios de Aceptación** | 1. El sistema debe mostrar el listado de disciplinas con su respectivo aforo antes de confirmar la matrícula.<br>2. El sistema debe descontar un cupo automáticamente al completarse una matrícula.<br>3. El sistema debe emitir un mensaje de alerta en consola cuando la disciplina no cuente con cupos disponibles. |
| **Restricciones** | No se permite el registro de dos clientes con el mismo número de documento de identidad (ID único). |

## Historia de Usuario 03

| Campo | Detalle |
|---|---|
| **Prioridad** | Alta |
| **Código del requerimiento** | RF03 |
| **Nombre del requerimiento** | Módulo de Matrículas y Control de Aforo |
| **Actor** | Administrador del Gimnasio |
| **Descripción** | Como administrador puedo matricular a un cliente previamente inscrito en una disciplina específica con el fin de controlar la asistencia y garantizar que no se supere el aforo máximo permitido. |
| **Funcionalidad** | Consultar la lista de disciplinas disponibles (Yoga, Pilates, Piscina, etc.), verificar la cantidad de cupos disponibles y asociar la matrícula del cliente disminuyendo en 1 la capacidad disponible. |
| **Criterios de Aceptación** | 1. El sistema debe mostrar el listado de disciplinas con su respectivo aforo antes de confirmar la matrícula.<br>2. El sistema debe descontar un cupo automáticamente al completarse una matrícula.<br>3. El sistema debe emitir un mensaje de alerta en consola cuando la disciplina no cuente con cupos disponibles. |
| **Restricciones** | Un cliente solo puede matricularse en una disciplina si ha sido registrado previamente en el sistema y si la disciplina cuenta con cupos mayores a cero. |

## Historia de Usuario 04

| Campo | Detalle |
|---|---|
| **Prioridad** | Media |
| **Código del requerimiento** | RF04 |
| **Nombre del requerimiento** | Módulo de Reportes e Informes |
| **Actor** | Administrador del Gimnasio |
| **Descripción** | Como administrador puedo consultar e imprimir reportes generales en consola con el fin de conocer el estado de ocupación del gimnasio y el listado de clientes activos. |
| **Funcionalidad** | Recorrer los diccionarios de datos del sistema para formatear y presentar en pantalla listas consolidadas de clientes inscritos, disciplinas con mayor demanda y niveles de aforo actualizados. |
| **Criterios de Aceptación** | 1. El sistema debe listar la totalidad de los clientes con su respectiva información personal.<br>2. El sistema debe mostrar el conteo de clientes matriculados por cada disciplina.<br>3. El sistema debe mostrar el porcentaje o cantidad de aforo disponible por clase. |
| **Restricciones** | Si no existen clientes registrados o disciplinas creadas, el sistema debe indicar mediante un mensaje claro que no hay datos para generar el reporte. |
