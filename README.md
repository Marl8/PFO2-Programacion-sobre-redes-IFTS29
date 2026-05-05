## PFO 2 Programación sobre Redes IFTS nº 29

El proyecto fue realizado como práctica formativa obligatoria en el marco de la carrera Tecnicatura Superior en Desarrollo de Software en el IFTS nº 29. La misma consta de una API en Python desarrollada con el Framework Flask con un cliente por consola y también con acceso web utilizando SQLite como base de datos.

### Estructura del proyecto

```text
PFO 2/
│── app.py
│
│── client.py 
│
│── config/
│   └── config.py
│
├── data/
│   └── db.py
│
├── models/
│   └── user_model.py
│
├── repositories/
│   └── user_repository.py
│
├── services/
│   └── auth_service.py
│
├── routes/
│   └── auth_routes.py
│
└── PFO2.db
```

### ⚙️ Instalación

**1.** Clonar o descargar el proyecto

````bash
git clone https://github.com/Marl8/PFO2-Programacion-sobre-redes-IFTS29.git
cd proyecto
````
**2.** Instalar dependencias

````bash
pip install -r requirements.txt
````
**3.** ▶️ Ejecutar el servidor

````bash
python app.py
````

El servidor correrá en ``http://127.0.0.1:5000``

**4.** 💻 Ejecutar el cliente

En otra terminal:

````bash
python client.py
````

### Conceptos implementados

- API REST con Flask.
- Separación de responsabilidades (MVC + Services + Repository).
- Persistencia con SQLite.
- Hash de contraseñas utilizando la biblioteca `werkzeug.security`.
- Cliente en consola.

### Usuarios de Prueba registrados en el sistema

- **Username:** "admin"

    **Password:** "admin"

- **Username:** "nombre"

    **Password:** "1234"