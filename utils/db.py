import sqlite3

def get_connection():
    return sqlite3.connect("data/escola.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    
    # Estudantes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes (
            matricula INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            nota1 FLOAT NOT NULL,
            nota2 FLOAT NOT NULL
        )                   
    """)

    # Documentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_upload TEXT
        )
    """)    
    conn.commit()

    # Usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()

    # Cria o usuário admin padrão se ele não existir
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", ("admin",))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", ("admin", "admin"))
        conn.commit()

    conn.close()