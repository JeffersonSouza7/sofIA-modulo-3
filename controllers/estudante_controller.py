from utils.db import get_connection
from models.estudante_model import Estudante

def adicionar_estudante(nome, idade, nota1, nota2):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO estudantes (nome, idade, nota1, nota2) VALUES (?, ?, ?, ?)""", 
                   (nome, idade, nota1, nota2))
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT matricula, nome, idade, nota1, nota2 FROM estudantes")
    rows = cursor.fetchall()
    conn.close()
    return [Estudante(*row) for row in rows]
