from data.db import get_db
from models.user_model import User

def create_user(usuario, password):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO usuarios (usuario, password) VALUES (?, ?)",
        (usuario, password)
    )
    db.commit()

def get_user_by_username(usuario):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = ?",
        (usuario,)
    )
    row = cursor.fetchone()

    if row:
        return User(row["id"], row["usuario"], row["password"])
    return None