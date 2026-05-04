from flask import Flask
from data.db import init_db, close_db
from routes.auth_routes import auth_bp

app = Flask(__name__)

# Registrar rutas
app.register_blueprint(auth_bp)

# Cerrar DB automáticamente
app.teardown_appcontext(close_db)

@app.route("/")
def principal():
    return """
    <h1>Inicie sesión para ingresar al sistema</h1>
    """

if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)