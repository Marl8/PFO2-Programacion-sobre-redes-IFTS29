from werkzeug.security import generate_password_hash, check_password_hash
from repositories.user_repository import create_user, get_user_by_username
import sqlite3

def register_user(usuario, password):
    hashed = generate_password_hash(password)

    try:
        create_user(usuario, hashed)
        return {"mensaje": "Usuario creado"}, 201
    except sqlite3.IntegrityError:
        return {"error": "Usuario ya existe"}, 400


def login_user(usuario, password):
    user = get_user_by_username(usuario)

    if user and check_password_hash(user.password, password):
        return {"mensaje": "Login exitoso", "usuario": usuario}, 200
    return {"error": "Credenciales inválidas"}, 401


def authenticate_user(usuario, password):
    user = get_user_by_username(usuario)

    if user and check_password_hash(user.password, password):
        return user
    return None