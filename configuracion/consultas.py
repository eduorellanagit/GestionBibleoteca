from configuracion import conexion

SQL_LIBROS = (
    "SELECT lb.id, lb.titulo, au.nombre, lb.isbn, lb.anio, lb.stock, "
    "lb.id_categoria, ct.nombre, lb.id_autor "
    "FROM t_libros lb "
    "JOIN t_categorias ct ON lb.id_categoria = ct.id "
    "JOIN t_autores au ON lb.id_autor = au.id "
)


ORDENES_LIBROS = ["lb.id", "lb.titulo", "lb.anio", "au.nombre"]


# --- CATEGORIAS ---

def func_listar_categorias():
    return conexion.conn.execute("SELECT id, nombre FROM t_categorias ORDER BY nombre").fetchall()


def func_obtener_categoria(id_cat):
    return conexion.conn.execute("SELECT id, nombre FROM t_categorias WHERE id = ?", (id_cat,)).fetchone()


def func_insertar_categoria(nombre):

    conexion.conn.execute("INSERT INTO t_categorias (nombre) VALUES (?)", (nombre,))
    conexion.conn.commit()


def func_existe_categoria_nombre(nombre, excluir_id = 0):

    fila = conexion.conn.execute(
        "SELECT 1 FROM t_categorias WHERE LOWER(nombre) = LOWER(?) AND id <> ?",
        (nombre, excluir_id)).fetchone()

    return fila is not None


def func_contar_libros_categoria(id_cat):
    return conexion.conn.execute("SELECT COUNT(*) FROM t_libros WHERE id_categoria = ?", (id_cat,)).fetchone()[0]


def func_actualizar_categoria(id_cat, nombre):

    conexion.conn.execute("UPDATE t_categorias SET nombre = ? WHERE id = ?", (nombre, id_cat))
    conexion.conn.commit()


def func_eliminar_categoria(id_cat):

    conexion.conn.execute("DELETE FROM t_categorias WHERE id = ?", (id_cat,))
    conexion.conn.commit()


# --- AUTORES ---

def func_listar_autores():
    return conexion.conn.execute("SELECT id, nombre FROM t_autores ORDER BY nombre").fetchall()


def func_obtener_autor(id_autor):
    return conexion.conn.execute("SELECT id, nombre FROM t_autores WHERE id = ?", (id_autor,)).fetchone()


def func_insertar_autor(nombre):

    conexion.conn.execute("INSERT INTO t_autores (nombre) VALUES (?)", (nombre,))
    conexion.conn.commit()


def func_existe_autor_nombre(nombre, excluir_id = 0):

    fila = conexion.conn.execute(
        "SELECT 1 FROM t_autores WHERE LOWER(nombre) = LOWER(?) AND id <> ?",
        (nombre, excluir_id)).fetchone()

    return fila is not None


def func_contar_libros_autor(id_autor):
    return conexion.conn.execute("SELECT COUNT(*) FROM t_libros WHERE id_autor = ?", (id_autor,)).fetchone()[0]


def func_actualizar_autor(id_autor, nombre):

    conexion.conn.execute("UPDATE t_autores SET nombre = ? WHERE id = ?", (nombre, id_autor))
    conexion.conn.commit()


def func_eliminar_autor(id_autor):

    conexion.conn.execute("DELETE FROM t_autores WHERE id = ?", (id_autor,))
    conexion.conn.commit()


# --- LIBROS ---

def func_listar_libros(opcion = 2):

    orden = ORDENES_LIBROS[opcion - 1]

    return conexion.conn.execute(SQL_LIBROS + "ORDER BY " + orden + ", lb.titulo").fetchall()


def func_obtener_libro(id_libro):
    return conexion.conn.execute(SQL_LIBROS + "WHERE lb.id = ?", (id_libro,)).fetchone()


def func_existe_isbn(isbn, excluir_id = 0):

    fila = conexion.conn.execute(
        "SELECT 1 FROM t_libros WHERE isbn = ? AND id <> ?",
        (isbn, excluir_id)).fetchone()

    return fila is not None


def func_insertar_libro(titulo, id_autor, isbn, anio, stock, id_cat):

    conexion.conn.execute(
        "INSERT INTO t_libros (titulo, id_autor, isbn, anio, stock, id_categoria) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (titulo, id_autor, isbn, anio, stock, id_cat))

    conexion.conn.commit()


def func_actualizar_libro(id_libro, titulo, id_autor, isbn, anio, stock, id_cat):

    conexion.conn.execute(
        "UPDATE t_libros SET titulo = ?, id_autor = ?, isbn = ?, anio = ?, "
        "stock = ?, id_categoria = ? WHERE id = ?",
        (titulo, id_autor, isbn, anio, stock, id_cat, id_libro))

    conexion.conn.commit()


def func_eliminar_libro(id_libro):

    conexion.conn.execute("DELETE FROM t_libros WHERE id = ?", (id_libro,))
    conexion.conn.commit()


def func_buscar_libros_por_titulo(texto):

    return conexion.conn.execute(
        SQL_LIBROS + "WHERE lb.titulo LIKE ? ORDER BY lb.titulo",
        (f"%{texto}%",)).fetchall()


def func_buscar_libros_por_autor(id_autor):

    return conexion.conn.execute(
        SQL_LIBROS + "WHERE lb.id_autor = ? ORDER BY lb.titulo",
        (id_autor,)).fetchall()


def func_buscar_libros_por_categoria(id_cat):

    return conexion.conn.execute(
        SQL_LIBROS + "WHERE lb.id_categoria = ? ORDER BY lb.titulo",
        (id_cat,)).fetchall()
