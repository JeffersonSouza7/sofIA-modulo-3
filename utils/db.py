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
    conn.close()
