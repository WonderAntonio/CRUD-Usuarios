# Aplicación CRUD con Python, Tkinter y SQLite

Sistema de escritorio desarrollado en Python que implementa una interfaz gráfica de usuario (GUI) utilizando **Tkinter** y una base de datos local con **SQLite**, estructurado bajo el patrón de diseño **MVC (Modelo-Vista-Controlador)**.

## Características

- **Conexión y Creación de Base de Datos:** Genera automáticamente la tabla de usuarios si no existe.
- **Operaciones CRUD Completas:**
  - **Create:** Inserta nuevos registros de usuarios (Nombre, Contraseña, Apellido, Dirección, Comentarios).
  - **Read:** Consulta registros existentes filtrando por ID.
  - **Update:** Modifica la información de un usuario existente.
  - **Delete:** Elimina registros de la base de datos.
- **Interfaz Modular:** Código dividido limpiamente en Modelos, Vistas y Controladores.

## Tecnologías utilizadas

- **Python 3.x**
- **Tkinter** (Lota nativa para interfaces gráficas)
- **SQLite3** (Gestión de base de datos ligera)

## Estructura del Proyecto

```text
Crud-Tkinter-SQLite/
│
├── controllers/
│   └── user_controller.py   # Lógica de negocio y manejo de eventos
├── models/
│   └── database.py          # Conexión y consultas SQL
├── views/
│   └── user_view.py         # Interfaz gráfica (Tkinter)
├── .gitignore
├── main.py                  # Archivo principal de ejecución
└── README.md
```
