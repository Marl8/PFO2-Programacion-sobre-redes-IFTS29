from flask import Blueprint, request, Response, jsonify
from services.auth_service import register_user, login_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    usuario = data.get("usuario")
    password = data.get("contraseña")

    res, status = register_user(usuario, password)
    return jsonify(res), status

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    password = data.get("contraseña")

    res, status = login_user(usuario, password)
    return jsonify(res), status

def unauthorized():
    return Response(
        "No autorizado",
        401,
        {"WWW-Authenticate": 'Basic realm="Login requerido"'}
    )

@auth_bp.route("/tareas", methods=["GET"])
def tareas():
    auth = request.authorization

    if not auth:
        return unauthorized()
    
    user = authenticate_user(auth.username, auth.password)

    if not user:
        return unauthorized()

    return f"""
    <h1>Bienvenido {user.usuario}</h1>
    <p>Sistema de tareas funcionando...</p>
    """