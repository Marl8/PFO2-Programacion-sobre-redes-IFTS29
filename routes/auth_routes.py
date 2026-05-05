from flask import Blueprint, request, Response, jsonify
from services.auth_service import register_user, login_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

# Ruta Registro
@auth_bp.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    usuario = data.get("usuario")
    password = data.get("contraseña")

    res, status = register_user(usuario, password)
    return jsonify(res), status


# Ruta login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    password = data.get("contraseña")

    res, status = login_user(usuario, password)
    return jsonify(res), status


# Ruta Tareas
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
    
# Si no esta autenticado envia un código 401 y un encabezado "WWW-Authenticate" del tipo Basic
# al navegador para activar su mecanismo de autenticación y poder ingresar las credenciales
# para el acceso al sistema 
def unauthorized():
    return Response(
        "No autorizado",
        401,
        {"WWW-Authenticate": 'Basic realm="Login requerido"'} 
    )    