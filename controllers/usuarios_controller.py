from utils.db import get_connection

def autenticar_usuario(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# CREATE
def criar_usuario(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

# READ
def listar_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# UPDATE
def atualizar_usuario(user_id, novo_username, nova_senha):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE usuarios SET username = ?, password = ? WHERE id = ?", (novo_username, nova_senha, user_id))
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()

# DELETE
def deletar_usuario(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
