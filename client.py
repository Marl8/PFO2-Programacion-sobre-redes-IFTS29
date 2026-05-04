import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:5000"
usuario_logueado = None

def registro():
    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    try:
        res = requests.post(f"{BASE_URL}/registro", json={
            "usuario": usuario,
            "contraseña": password
        })
        print("STATUS:", res.status_code)
        print("RESPUESTA:", res.json())

    except Exception as e:
        print("Error:", e)

def login():
    global usuario_logueado

    usuario = input("Usuario: ")
    password = input("Contraseña: ")

    res = requests.post(f"{BASE_URL}/login", json={
        "usuario": usuario,
        "contraseña": password
    })
    print("STATUS:", res.status_code)
    print("RESPUESTA:", res.json())

    if res.status_code == 200:
        usuario_logueado = {"usuario": usuario, "password": password}
        print("Sesión iniciada")
    else:
        print("Login falló")


def ver_tareas():
    try:
        res = requests.get(
            f"{BASE_URL}/tareas",
            auth=HTTPBasicAuth(
                usuario_logueado["usuario"],
                usuario_logueado["password"]
            )
        )
        print("STATUS:", res.status_code)
        print(res.text)
    except Exception as e:
        print("Error:", e)

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Registro")
        print("2. Login")
        print("3. Ver tareas")
        print("4. Salir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            registro()
        elif opcion == "2":
            login()
        elif opcion == "3":
            if not usuario_logueado:
                print("Debe loguearse primero")
            else:
                print("Accediendo al sistema...")
                ver_tareas()    
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()