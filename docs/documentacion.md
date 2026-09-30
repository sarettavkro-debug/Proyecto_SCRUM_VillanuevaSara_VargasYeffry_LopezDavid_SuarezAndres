
# PROYECTO: Sistema de Gestión - Gimnasio ForceTech

**Integrantes:**
* Juan Andrés Suárez (Dev 1)
* Yeffry Vargas (Dev 2)
* David López (Dev 3)
* Sara Villanueva Caro (Dev 4)

**Asignatura:** Scrum y Metodologías ágiles<br>**Docente:** Kevin Johan Jimenez Delgado<br>**Institución:** Campuslands<br>**Grupo asignado:** Grupo 4 - Z1 

---

## 1. SITUACIÓN PROBLEMA

El Gimnasio ForceTech enfrenta actualmente la necesidad de optimizar y centralizar el seguimiento y control de sus clientes y servicios ofrecidos. La falta de un sistema automatizado dificulta la captura precisa de datos personales, la clasificación de niveles de riesgo físico de los usuarios, el control estricto del aforo máximo en disciplinas (como Yoga, Pilates, Piscina, Gimnasio general y Entrenamiento personalizado) y la generación oportuna de reportes operativos.

Para dar solución a esta problemática, el equipo de desarrollo implementa una aplicación en Python bajo el marco de trabajo ágil SCRUM. Esta solución permite gestionar inscripciones, controlar cupos en tiempo real, asignar instructores y evaluar periódicamente el progreso físico de los clientes con los más altos estándares de calidad.

---

## 2. LEVANTAMIENTO DE REQUERIMIENTOS

El proceso de levantamiento de requerimientos para el sistema ForceTech se llevó a cabo mediante el análisis de las necesidades operativas del gimnasio. Se identificó la urgencia de automatizar el registro de clientes, la asignación de cupos por disciplina y el control en tiempo real del aforo máximo permitido para garantizar la calidad del servicio e identificar clientes con niveles de riesgo alto.

---

## 3. REQUERIMIENTOS 

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

## 4. HISTORIAS DE USUARIO CON CRITERIOS DE ACEPTACIÓN

A continuación se detallan las Historias de Usuario (HU) definidas para el desarrollo del sistema ForceTech, extraídas del Backlog del proyecto:

### HISTORIA DE USUARIO 01 (Tarjeta #1)
| Campo | Detalle |
|---|---|
| **Prioridad** | Alta |
| **Código del requerimiento** | RNF01 / RNF02 / RNF03 |
| **Nombre del requerimiento** | Configuración de Entorno y Arquitectura Base |
| **Actor** | Equipo de Desarrollo / Scrum Master |
| **Descripción** | Como equipo de desarrollo quiero configurar el entorno de trabajo inicial y la estructura de archivos base (`backend/`, `docs/`, `tests/`) con el fin de garantizar el orden del proyecto y el control de versiones colaborativo en GitHub. |
| **Funcionalidad** | Creación del repositorio, configuración de ramas locales/remotas, archivo `.gitignore` e inicialización de la arquitectura de código modular en Python (`modelos.py`, `inscripciones.py`, `matriculas.py`, `reportes.py`). |
| **Criterios de Aceptación** | 1. El repositorio debe contar con la rama principal `main` y las ramas de trabajo por desarrollador.<br>2. La estructura de carpetas debe separar claramente el código fuente (`backend/`), la documentación (`docs/`) y las pruebas (`tests/`).<br>3. El archivo `.gitignore` debe omitir archivos temporales y entornos virtuales de Python. |
| **Restricciones** | Ningún desarrollador puede realizar commits o cambios directos sobre la rama `main` sin la aprobación de un Pull Request (PR). |

---

### HISTORIA DE USUARIO 02 (Tarjeta #2)
| Campo | Detalle |
|---|---|
| **Prioridad** | Alta |
| **Código del requerimiento** | RF01 – Gestión de Clientes |
| **Nombre del requerimiento** | Módulo de Clientes e Inscripciones |
| **Actor** | Administrador del Gimnasio |
| **Descripción** | Como administrador puedo registrar nuevos clientes capturando su información personal con el fin de mantener un control actualizado de los usuarios activos y su nivel de riesgo en el gimnasio. |
| **Funcionalidad** | Permitir el ingreso de datos en la consola para registrar ID, nombres, apellidos, dirección, teléfonos de contacto, estado y nivel de riesgo (Alto, Medio, Bajo), guardándolos en diccionarios dentro de `backend/inscripciones.py`. |
| **Criterios de Aceptación** | 1. El sistema debe solicitar y capturar todos los campos obligatorios del cliente mediante la terminal.<br>2. El sistema debe validar que el nivel de riesgo asignado sea únicamente 'Alto', 'Medio' o 'Bajo'.<br>3. El sistema debe confirmar la recepción exitosa guardando el cliente en memoria. |
| **Restricciones** | El sistema no debe permitir el registro de dos clientes con el mismo ID (control de duplicados). |

---

### HISTORIA DE USUARIO 03 (Tarjeta #3)
| Campo | Detalle |
|---|---|
| **Prioridad** | Alta |
| **Código del requerimiento** | RF02 – Catálogo de Servicios / RF03 – Módulo de Matrículas |
| **Nombre del requerimiento** | Módulo de Matrículas y Control de Aforo |
| **Actor** | Administrador del Gimnasio |
| **Descripción** | Como administrador puedo matricular a un cliente registrado en alguno de los 5 servicios disponibles con el fin de controlar la asistencia y evitar que se supere la capacidad máxima (aforo). |
| **Funcionalidad** | Desplegar la lista de servicios con sus cupos disponibles en `backend/matriculas.py`, asociar la matrícula del cliente y actualizar automáticamente la disponibilidad restando un cupo del aforo máximo. |
| **Criterios de Aceptación** | 1. El sistema debe mostrar el catálogo con los 5 servicios ofrecidos y su capacidad actual.<br>2. Al concretar una matrícula, el sistema debe descontar de inmediato 1 cupo disponible del servicio seleccionado.<br>3. El sistema debe emitir un mensaje de alerta cuando el usuario intente matricular en una clase sin cupos libres. |
| **Restricciones** | Solo se pueden matricular clientes previamente inscritos en el sistema (RF01) y en servicios cuyos cupos disponibles sean mayores a cero. |

---

### HISTORIA DE USUARIO 04 (Tarjeta #4)
| Campo | Detalle |
|---|---|
| **Prioridad** | Media |
| **Código del requerimiento** | RF04 – Módulo de Reportes |
| **Nombre del requerimiento** | Módulo de Reportes e Informes |
| **Actor** | Administrador del Gimnasio / Entrenador |
| **Descripción** | Como administrador puedo generar e imprimir reportes consolidados en consola con el fin de evaluar la ocupación general del gimnasio e identificar usuarios con nivel de riesgo alto. |
| **Funcionalidad** | Recorrer los diccionarios del sistema desde `backend/reportes.py` para listar clientes inscritos, servicios activos, porcentaje/aforo ocupado y un reporte específico de usuarios con riesgo 'Alto'. |
| **Criterios de Aceptación** | 1. El sistema debe listar la totalidad de los clientes con sus datos personales e información de contacto.<br>2. El sistema debe mostrar la capacidad máxima y los cupos ocupados por cada uno de los servicios.<br>3. El sistema debe ofrecer una opción de filtrado para desplegar de forma independiente los clientes clasificados con nivel de riesgo 'Alto'. |
| **Restricciones** | Si la base de datos en memoria no cuenta con registros, el sistema debe mostrar una advertencia indicando la ausencia de datos en lugar de arrojar un error de ejecución. |

---

### HISTORIA DE USUARIO 05 (Tarjeta #5)
| Campo | Detalle |
|---|---|
| **Prioridad** | Alta |
| **Código del requerimiento** | RNF01 / RNF02 / RNF03 |
| **Nombre del requerimiento** | Documentación SCRUM y Requerimientos |
| **Actor** | Scrum Master |
| **Descripción** | Como Scrum Master puedo redactar la documentación metodológica e integrar las evidencias en `docs/documentacion.md` para garantizar la trazabilidad y transparencia del proyecto bajo el marco SCRUM. |
| **Funcionalidad** | Registrar el planteamiento del problema, requerimientos (RF y RNF), Historias de Usuario, bitácoras de Daily Stand-ups y capturas de pantalla del flujo de trabajo en el tablero Kanban (Días 1 a 5). |
| **Criterios de Aceptación** | 1. El archivo `docs/documentacion.md` debe estar estructurado según el índice oficial de la guía.<br>2. Debe incluir las 6 Historias de Usuario con sus respectivos criterios de aceptación y restricciones.<br>3. Debe evidenciar la evolución del tablero Kanban día por día mediante imágenes y descripciones detalladas. |
| **Restricciones** | La documentación debe mantenerse actualizada de forma diaria al cierre de cada jornada de trabajo. |

---

### HISTORIA DE USUARIO 06 (Tarjeta #6)
| Campo | Detalle |
|---|---|
| **Prioridad** | Media |
| **Código del requerimiento** | RNF01 – Usabilidad / RNF03 – Integridad de Datos |
| **Nombre del requerimiento** | Integración Final y Pruebas del Sistema |
| **Actor** | Equipo de Desarrollo / QA |
| **Descripción** | Como equipo de desarrollo queremos integrar todos los módulos en el ejecutable principal (`main.py`) y validar la matriz de pruebas (CP01-CP08) para entregar un sistema funcional y libre de fallas. |
| **Funcionalidad** | Unificar `inscripciones.py`, `matriculas.py` y `reportes.py` en un menú numérico en consola (RNF01) y registrar los casos de prueba superados en `tests/pruebas.md`. |
| **Criterios de Aceptación** | 1. El menú en `main.py` debe permitir navegar por todas las funciones del sistema usando opciones numéricas.<br>2. El sistema debe validar las entradas incorrectas o vacías del usuario sin interrumpir ni cerrar el programa.<br>3. Los 8 Casos de Prueba (CP01 al CP08) deben estar documentados y evaluados como aprobados en `tests/pruebas.md`. |
| **Restricciones** | La integración final solo se dará por concluida cuando todas las ramas se hayan fusionado en `main` sin conflictos de código. |

---

## 5. METODOLOGÍA (MARCO DE TRABAJO SCRUM)

El desarrollo de la aplicación para el Gimnasio ForceTech se gestiona mediante la metodología ágil SCRUM, organizada en un ciclo de desarrollo de 5 días con 2 Sprints operativos.

### 5.1 Definición de Roles

* **Product Owner:** Encargado de priorizar el Product Backlog y definir los criterios de aceptación para las funcionalidades del gimnasio.
* **Scrum Master (Sara Villanueva):** Lidera la gestión del tablero en GitHub Projects, facilita los Daily Stand-ups, remueve bloqueos técnicos, coordina la integración del equipo y apoya el desarrollo técnico.
* **Equipo de Desarrollo (Developers):**
  * **Juan Andrés Suárez (Dev 1):** Arquitectura base y modelos (`backend/modelos.py`).
  * **Yeffry Vargas (Dev 2):** Módulo de inscripciones y registro de clientes (`backend/inscripciones.py`).
  * **David López (Dev 3):** Módulo de matrículas y control de aforo (`backend/matriculas.py`).
  * **Sara Villanueva (Dev 4):** Módulo de reportes (`backend/reportes.py`) y consolidación de la documentación oficial.

### 5.2 Eventos

* **Sprint Planning:** Definición del alcance e historias de usuario seleccionadas para cada Sprint.
* **Daily Stand-up:** Reuniones diarias de 10 minutos para revisar avances en el tablero Kanban y coordinar integraciones.
* **Sprint Review & Retrospective:** Demostración del incremento funcional e identificación de mejoras para la siguiente iteración.

### 5.3 Artefactos

* **Product Backlog:** Lista priorizada que contiene la totalidad de los requerimientos funcionales y no funcionales del Gimnasio ForceTech (RF01 a RF04 y RNF01 a RNF03), representada en las Historias de Usuario iniciales.
* **Sprint Backlog:** Conjunto de tareas e historias de usuario seleccionadas específicamente desde el Product Backlog para ejecutarse durante los Sprints del proyecto, asignadas individualmente en el tablero Kanban.
* **Increment:** La versión funcional del software entregada al final de cada Sprint. En el proyecto corresponde al sistema ejecutable en Python (`main.py`) integrado con sus módulos y la documentación oficial finalizada.

---

## 6. EVIDENCIA DE PLANTEAMIENTO DE PLATAFORMA DE TRABAJO

### 6.1 Estructura del Tablero Kanban (GitHub Projects)
El proyecto cuenta con un tablero Kanban configurado con 5 estados de flujo de trabajo:
1. **Reserva (Backlog):** Tareas pendientes para Sprints futuros.
2. **Por Hacer (Sprint Backlog):** Tareas priorizadas para el Sprint activo.
3. **En Curso (In Progress):** Tareas en desarrollo activo.
4. **En Revisión (In Review):** Tareas pendientes de verificación o Pull Request.
5. **Hecho (Done):** Tareas finalizadas y probadas.

### 6.2 Capturas y Estado del Tablero (Día 1)

![Captura](<../Imagenes/Kanban dia 1 actualizado.0.png>)

* **Organización por Sprints:**
  * **Sprint 1 (Días 1 a 3):** Enfocado en configuración, modelos de datos, inscripciones de clientes y matrículas con control de aforo.
  * **Sprint 2 (Días 4 y 5):** Enfocado en generación de reportes, pruebas cruzadas e integración final.
* **Metadatos asignados:** Cada tarjeta cuenta con sus respectivos responsables (*Assignees*), etiquetas de clasificación (`backend`, `documentation`, `setup`, `testing`) y la iteración asignada.

Al finalizar el Día 1, el tablero Kanban refleja el inicio de las actividades y la preparación de la arquitectura base del proyecto para el Sprint 1:

* **Reserva (Backlog):** Se mantienen aisladas las tarjetas **#4** (Módulo de Reportes e Informes) y **#6** (Integración Final y Pruebas del Sistema), reservadas para su ejecución en el Sprint 2.
* **Por Hacer (Sprint Backlog):** Tarjetas **#2** (Módulo de Clientes e Inscripciones) y **#3** (Módulo de Matrículas y Aforo), priorizadas y preparadas para iniciar su desarrollo técnico en los siguientes días del Sprint 1.
* **En Curso (In Progress):** Tarjeta **#5** (Documentación SCRUM y Requerimientos), asignada a **Dev 4** para la elaboración de la estructura documental, requerimientos y bitácoras del proyecto.
* **En Revisión (In Review):** Columna despejada sin elementos pendientes de validación.
* **Hecho (Done)** Tarjeta **#1** (Configuración de Entorno y Arquitectura Base), completada exitosamente al dejar lista la estructura inicial de repositorio, ramas y carpetas del proyecto.

### 6.3 Evidencias del Tablero - Día 2

![Captura 2](<../Imagenes/Kanban día 2 actualizado.png>)

Al finalizar el Día 2, el tablero Kanban refleja el inicio de los trabajos de desarrollo técnico del Sprint 1:

* **Reserva (Backlog):** Se mantienen las tarjetas #4 (Reportes) y #6 (Integración final) asignadas para el Sprint 2.
* **Por Hacer (Sprint Backlog):** Tarjeta #3 (Módulo de Matrículas) lista para el Día 3.
* **En Curso (In Progress):** Tarjeta #2 (Módulo de Usuarios e Inscripciones) en desarrollo activo por Dev 2 y Dev 1. Tarjeta #5 (Documentación y Requerimientos por Dev 4).
* **Hecho (Done):** Tarjeta #1 (Configuración de entorno).

### 6.4 Evidencias del Tablero - Día 3 (Módulo de Matrículas y Control de Aforo)

![Captura 3](<../Imagenes/Kanban día 3.png>)

Al finalizar el Día 3, el tablero en GitHub Projects evidencia el avance y la culminación del desarrollo técnico correspondiente al **Sprint 1**:

* **Reserva (Backlog):** Se mantienen aisladas las Tarjetas **#4** (Módulo de Reportes) y **#6** (Integración final y entrega), las cuales se activarán al inicio del Sprint 2 (Días 4 y 5).
* **Reserva (Backlog):** Columna despejada debido a que todas las historias del Sprint 1 han pasado a fase de ejecución o revisión.
* **Por Hacer (Sprint Backlog):** 
  * **Tarjeta #3 (Módulo de Matrículas y Control de Aforo):** Asignada a **Dev 3**, enfocada en la programación de la lógica en `backend/matriculas.py` para la validación de cupos máximos por disciplina.
* **En Revisión (In Review):** 
  * **Tarjeta #2 (Módulo de Inscripciones y Clientes):** Asignada a **Dev 2**, en proceso de revisión de código y validación del Pull Request hacia la rama principal (`main`).
  * **Tarjeta #5:** Documentación técnica, Requerimientos (RF/RNF) y gestión del marco SCRUM por el Scrum Master (Dev 4).
* **Hecho (Done):** 
  * **Tarjeta #1:** Configuración inicial del proyecto y entorno de trabajo.

### 6.5 Evidencias del Tablero - Día 4 (Módulo de Reportes e Informes)

![captura 4](<../Imagenes/Kanban día 4.png>)

Al iniciar el Día 4, el tablero en GitHub Projects evidencia la transición y el arranque del desarrollo técnico correspondiente al **Sprint 2**:

* **Reserva (Backlog):** Columna despejada debido a que todas las historias de usuario del proyecto han sido priorizadas y movidas al flujo de trabajo del Sprint 2.
* **Por Hacer (Sprint Backlog):** 
  * **Tarjeta #6 (Integración Final y Pruebas del Sistema):** Pendiente a la espera de finalizar la lógica del módulo de reportes para realizar la integración integral del programa.
* **En Curso (In Progress):**
  * **Tarjeta #4 (Módulo de Reportes e Informes):** Asignada a **Dev 2** y **Dev 3**, enfocada en la programación de los algoritmos de consulta para mostrar la lista de clientes y el estado de ocupación por disciplina en consola.
  * **Tarjeta #5:** Documentación técnica, Requerimientos (RF/RNF) y gestión del marco SCRUM por el Scrum Master (**Dev 4**).
* **En Revisión (In Review):**
  * **Tarjeta #3 (Módulo de Matrículas y Control de Aforo):** Asignada a **Dev 3**, en proceso de revisión de código y validación del Pull Request hacia la rama principal (`main`) por parte de **Dev 1**.
* **Hecho (Done):**
  * **Tarjeta #1:** Configuración inicial del proyecto y entorno de trabajo.
  * **Tarjeta #2 (Módulo de Inscripciones y Clientes):** Integrada exitosamente en la rama principal (`main`).

### 6.6 Evidencias del Tablero - Día 5 (Cierre del Sprint 2 y Entrega Final)

![Captura día 5](<../Imagenes/Tablero de kanban ultimo dia .png>)

Al finalizar el Día 5, el tablero Kanban en GitHub Projects evidencia el cumplimiento total del alcance del proyecto y la culminación del **Sprint 2**:

* **Reserva (Backlog):** Columna despejada.
* **Por hacer:** Columna despejada.
* **En curso:** Columna despejada.
* **En revisión:** Columna despejada debido a que todos los Pull Requests han sido aprobados e integrados a la rama principal (`main`).
* **Hecho:** 
  * **Tarjeta #1:** Configuración inicial del proyecto y entorno de trabajo.
  * **Tarjeta #2 (Módulo de Inscripciones y Clientes):** Integrada y probada en `main`.
  * **Tarjeta #3 (Módulo de Matrículas y Control de Aforo):** Integrada y probada en `main`.
  * **Tarjeta #4 (Módulo de Reportes e Informes):** Programada e integrada exitosamente.
  * **Tarjeta #5 (Documentación y Marco SCRUM):** Documento final `docs/documentacion.md` completado con historias de usuario, requerimientos y bitácoras.
  * **Tarjeta #6 (Integración Final y Pruebas del Sistema):** Menú interactivo ensamblado en `main.py`, pruebas (CP01-CP08) superadas y `README.md` finalizado.

## 6.1. Bitácora de Seguimiento Diario (Daily Stand-ups)

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

#### 📌 Día 4: Módulo de Reportes e Informes (Inicio Sprint 2)
* **Fecha:** 29 de septiembre de 2026
* **Moderador:** Scrum Master (Dev 4)
* **Plan de trabajo y compromisos del día:**
  * **Dev 1:** Revisará y validará el Pull Request de la Tarjeta #3 para su integración a `main`, y apoyará las pruebas iniciales del módulo de reportes.
  * **Dev 2:** Desarrollará la lógica en `backend/reportes.py` para consultar y desplegar la lista general de clientes inscritos en consola.
  * **Dev 3:** Finalizará los ajustes de matrículas y colaborará con Dev 2 en los algoritmos para calcular el aforo y ocupación por disciplina.
  * **Dev 4 (Scrum Master):** Actualizará la documentación del proyecto en `docs/documentacion.md`, registrará las evidencias del inicio del Sprint 2 y organizará los entregables finales.
* **Bloqueos / Impedimentos reportados:** El desarrollador 2 (Yeffry) debía solucionar unos problemas de validaciones con la función registrar_cliente reportadas por el desarrollador 1 (Juan Andrés)
* **Estado del Tablero:** Tarjeta #3 movida a *En Revisión*; Tarjeta #4 movida a *En Curso*; Tarjeta #5 se mantiene *En Curso*.

#### 📌 Día 5: Integración Final, Pruebas y Cierre del Proyecto (Sprint 2)
* **Fecha:** 30 de septiembre de 2026
* **Moderador:** Scrum Master (Dev 4)
* **Plan de trabajo y compromisos del día:**
  * **Dev 1:** Ejecutará y documentará la matriz de casos de prueba (CP01 a CP08) en `tests/pruebas.md`, realizando la revisión final del código e integración a `main`.
  * **Dev 2:** Apoyará la revisión del archivo principal (`main.py`) para asegurar que las opciones del menú invocan correctamente los módulos de inscripciones.
  * **Dev 3:** Validará la correcta interacción entre la asignación de cupos y las alertas de aforo máximo en el menú consolidado del programa.
  * **Dev 4 (Scrum Master):** Finalizará la redacción del archivo `README.md`, consolidará la documentación oficial en `docs/documentacion.md` con las bitácoras y capturas finales, y verificará que el tablero Kanban tenga el 100% de las tarjetas en la columna *Hecho*.
* **Bloqueos / Impedimentos reportados:** Ninguno.
* **Estado del Tablero:** Tarjetas #3, #4, #5 y #6 aprobadas en revisión y movidas exitosamente a la columna *Hecho (Done)*. El 100% de las historias de usuario del proyecto han sido completadas.