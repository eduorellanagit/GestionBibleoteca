# Gestión de Biblioteca Escolar

Sistema de consola en **Python 3** para administrar los libros de una biblioteca escolar y sus categorías. Los datos se guardan de forma persistente en una base de datos **SQLite**.

Trabajo final de Python - ISET.

## Características

- Menú principal y submenús construidos con listas, con el nombre del sistema siempre visible arriba.
- **CRUD de libros:** listar, crear, modificar y eliminar.
- **CRUD de categorías:** listar, crear, modificar y eliminar (no permite borrar una categoría que tenga libros).
- **Búsquedas** de libros por título, por autor y por categoría.
- **Reportes:** ver el reporte actual en pantalla, guardarlo en la base de datos y buscar reportes guardados por año y mes.
- **Validación de datos** en todas las entradas del usuario.
- Código modular, separado en carpetas de funciones y de configuración.

## Requisitos

- Python 3 (no hace falta instalar ninguna librería externa: `sqlite3` ya viene incluido).

## Cómo ejecutarlo

1. Descargá o cloná el repositorio.
2. Abrí una terminal dentro de la carpeta del proyecto (donde está `main.py`).
3. Ejecutá:

```bash
python3 main.py
```

La base de datos `biblioteca.db` y sus tablas se crean automáticamente la primera vez.

## Estructura del proyecto

```
GestionBiblioteca/
├── main.py                       # Menús, submenús y flujo principal
├── configuracion/
│   ├── conexion.py               # Conexión a SQLite y creación de tablas
│   ├── consultas.py              # Consultas SQL de libros y categorías
│   └── consultas_reportes.py     # Consultas SQL de los reportes guardados
└── funciones/
    ├── libros.py                 # Alta, baja, modificación y búsquedas de libros
    ├── categorias.py             # CRUD de categorías
    ├── reportes.py               # Ver, guardar y buscar reportes
    ├── validaciones.py           # Validación de lo que escribe el usuario
    └── formato.py                # Armado de las tablas de texto
```

## Menús

```
MENÚ PRINCIPAL
1. Listar libros
2. Nuevo libro
3. Modificar libro
4. Buscar libro            -> por título / por autor / por categoría
5. Eliminar libro
6. Administrar categorías  -> listar / nueva / modificar / eliminar
7. Reportes                -> ver reporte / buscar reporte
0. Salir
```

- En el menú principal, **0 cierra el programa**. En los submenús, **0 vuelve** al menú anterior.
- En los formularios, **0 cancela** la operación y no se guarda ningún cambio.
- Los menús solo aceptan números enteros dentro del rango de opciones.

## Base de datos

| Tabla | Descripción |
|---|---|
| `t_categorias` | Categorías de los libros (nombre único). |
| `t_libros` | Libros, relacionados con su categoría mediante `id_categoria`. |
| `t_reportes` | Cabecera de cada reporte guardado: año, mes, fecha, hora y totales. |
| `t_reportes_detalle` | Copia de los libros al momento de guardar el reporte. |

El detalle de los reportes es una copia de los datos, sin relación con `t_libros`, por lo que un reporte guardado no cambia aunque después se modifique o se elimine un libro.

## Validaciones

- **ISBN:** 10 o 13 dígitos (se aceptan guiones) y no se puede repetir.
- **Año de publicación:** entre 1000 y el año actual.
- **Stock:** entre 1 y 999.
- **Categorías:** el nombre no se puede repetir.
- **Textos:** no pueden quedar vacíos ni superar el largo máximo.
- **Eliminaciones:** piden confirmación (`s/n`).
- **Búsqueda de reportes:** el año y el mes (1 a 12) se validan antes de consultar.
