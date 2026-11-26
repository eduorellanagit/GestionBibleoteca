
SQL_LIBROS = (
    "SELECT lb.id, lb.titulo, lb.autor, lb.isbn, lb.anio, lb.stock, "
    "lb.id_categoria, ct.nombre "
    "FROM t_libros lb JOIN t_categorias ct ON lb.id_categoria = ct.id "
)


# --- CATEGORIAS ---

def func_listar_categorias(conn):
    return conn.execute("SELECT id, nombre FROM t_categorias ORDER BY nombre").fetchall()


def func_obtener_categoria(conn, id_cat):
    return conn.execute("SELECT id, nombre FROM t_categorias WHERE id = ?", (id_cat,)).fetchone()


def func_insertar_categoria(conn, nombre):

    conn.execute("INSERT INTO t_categorias (nombre) VALUES (?)", (nombre,))
    conn.commit()


def func_existe_categoria_nombre(conn, nombre, excluir_id = 0):

    fila = conn.execute(
        "SELECT 1 FROM t_categorias WHERE LOWER(nombre) = LOWER(?) AND id <> ?",
        (nombre, excluir_id)).fetchone()

    return fila is not None


def func_contar_libros_categoria(conn, id_cat):
    return conn.execute("SELECT COUNT(*) FROM t_libros WHERE id_categoria = ?", (id_cat,)).fetchone()[0]


def func_actualizar_categoria(conn, id_cat, nombre):

    conn.execute("UPDATE t_categorias SET nombre = ? WHERE id = ?", (nombre, id_cat))
    conn.commit()


def func_eliminar_categoria(conn, id_cat):

    conn.execute("DELETE FROM t_categorias WHERE id = ?", (id_cat,))
    conn.commit()


# --- LIBROS ---

def func_listar_libros(conn):
    return conn.execute(SQL_LIBROS + "ORDER BY lb.titulo").fetchall()


def func_obtener_libro(conn, id_libro):
    return conn.execute(SQL_LIBROS + "WHERE lb.id = ?", (id_libro,)).fetchone()


def func_existe_isbn(conn, isbn, excluir_id = 0):

    fila = conn.execute(
        "SELECT 1 FROM t_libros WHERE isbn = ? AND id <> ?",
        (isbn, excluir_id)).fetchone()

    return fila is not None


def func_insertar_libro(conn, titulo, autor, isbn, anio, stock, id_cat):

    conn.execute(
        "INSERT INTO t_libros (titulo, autor, isbn, anio, stock, id_categoria) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (titulo, autor, isbn, anio, stock, id_cat))

    conn.commit()


def func_actualizar_libro(conn, id_libro, titulo, autor, isbn, anio, stock, id_cat):

    conn.execute(
        "UPDATE t_libros SET titulo = ?, autor = ?, isbn = ?, anio = ?, "
        "stock = ?, id_categoria = ? WHERE id = ?",
        (titulo, autor, isbn, anio, stock, id_cat, id_libro))

    conn.commit()


def func_eliminar_libro(conn, id_libro):

    conn.execute("DELETE FROM t_libros WHERE id = ?", (id_libro,))
    conn.commit()


def func_buscar_libros_por_titulo(conn, texto):

    return conn.execute(
        SQL_LIBROS + "WHERE lb.titulo LIKE ? ORDER BY lb.titulo",
        (f"%{texto}%",)).fetchall()


def func_buscar_libros_por_autor(conn, texto):

    return conn.execute(
        SQL_LIBROS + "WHERE lb.autor LIKE ? ORDER BY lb.titulo",
        (f"%{texto}%",)).fetchall()


def func_buscar_libros_por_categoria(conn, id_cat):

    return conn.execute(
        SQL_LIBROS + "WHERE lb.id_categoria = ? ORDER BY lb.titulo",
        (id_cat,)).fetchall()
