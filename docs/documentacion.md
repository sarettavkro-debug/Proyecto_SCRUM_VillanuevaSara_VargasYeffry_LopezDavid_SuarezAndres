Responsable: Desarrollador 4 – Scrum Master
# PROYECTO: Sistema de Gestión - Gimnasio ForceTech

**Integrantes:**
* Sara Villanueva Caro
* Yeffry Vargas
* David López
* Andrés Suárez

**Asignatura:** Ingeniería de Software  
**Institución:** Universidad de Santander (UDES)  
**Fecha:** Septiembre de 2026  

---

## 1. SITUACIÓN PROBLEMA

El Gimnasio ForceTech enfrenta actualmente la necesidad de optimizar y centralizar el seguimiento y control de sus clientes y servicios ofrecidos. La falta de un sistema automatizado dificulta la captura precisa de datos personales, la clasificación de niveles de riesgo físico de los usuarios, el control estricto del aforo máximo en disciplinas (como Yoga, Pilates, Piscina, Gimnasio general y Entrenamiento personalizado) y la generación oportuna de reportes operativos.

Para dar solución a esta problemática, el equipo de desarrollo implementa una aplicación en Python bajo el marco de trabajo ágil SCRUM. Esta solución permite gestionar inscripciones, controlar cupos en tiempo real, asignar instructores y evaluar periódicamente el progreso físico de los clientes con los más altos estándares de calidad.

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

#### 📌 Día 1: Kickoff, Configuración y Arquitectura Base
* **Fecha:** 26 de septiembre de 2026
* **Moderador:** Scrum Master (Dev 4)
* **Resumen de intervenciones:**
  * **Dev 1 & Dev 2:** Configuraron la estructura de carpetas, el archivo `backend/modelos.py` y el menú inicial en `main.py`.
  * **Dev 3:** Revisó la estructura de datos base para los módulos posteriores.
  * **Dev 4:** Creó y configuró el tablero Kanban en GitHub Projects, definiendo columnas, vistas, etiquetas y campos de Sprint.
* **Bloqueos / Impedimentos:** Ninguno.
* **Estado del Tablero:** Tarjeta #1 completada y movida a *Hecho*. Tarjetas del Sprint 1 asignadas.

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