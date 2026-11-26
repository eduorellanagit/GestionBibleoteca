
def func_insertar_reporte (conn, anio, mes, fecha, hora, total_titulos, total_stock, libros):

    cur = conn.execute (

        "INSERT INTO t_reportes (anio, mes, fecha, hora, total_titulos, total_stock) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (anio, mes, fecha, hora, total_titulos, total_stock)
        
    )

    id_reporte = cur.lastrowid

    for libro in libros:

        conn.execute (

            "INSERT INTO t_reportes_detalle "
            "(id_reporte, id_libro, titulo, autor, isbn, anio_publicacion, stock, categoria) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (id_reporte, libro[0], libro[1], libro[2], libro[3], libro[4], libro[5], libro[7])
            
        )

    conn.commit()



def func_buscar_reportes (conn, anio, mes):

    return conn.execute (

        "SELECT id, fecha, hora, total_titulos, total_stock "
        "FROM t_reportes WHERE anio = ? AND mes = ? ORDER BY id",
        (anio, mes)
        
    ).fetchall()



def func_listar_detalle_reporte (conn, id_reporte):

    return conn.execute (

        "SELECT id_libro, titulo, autor, isbn, anio_publicacion, stock, id_reporte, categoria "
        "FROM t_reportes_detalle WHERE id_reporte = ? ORDER BY titulo",
        (id_reporte,)
        
    ).fetchall()
