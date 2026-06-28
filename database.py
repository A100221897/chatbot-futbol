import sqlite3

DB = "football.db"


def conectar():
    return sqlite3.connect(DB)


def crear_bd():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT,
        respuesta TEXT
    )
    """)

    conn.commit()
    conn.close()


def guardar(pregunta, respuesta):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO consultas(pregunta,respuesta) VALUES(?,?)",
        (pregunta, respuesta)
    )

    conn.commit()
    conn.close()