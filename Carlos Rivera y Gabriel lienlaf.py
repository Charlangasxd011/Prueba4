lista = []
minimo_caracteres = 8

def registrar_usuario(lista):
    nombre = input("Ingrese nombre de usuario: ").strip()
    if nombre.lower() in [usuario["nombre"].lower() for usuario in lista]:
        print("Error: el usuario ya existe.")
        return  

    sexo = input("Ingrese sexo (M/F): ").strip().upper()
    if sexo not in ["M", "F"]:
        print("Sexo inválido. Solo se permite 'M' o 'F'.")
        return
    contrasena = input("Ingrese contraseña: ").strip()
    if not validar_contrasena(contrasena):
        print(f"La contraseña debe tener al menos {minimo_caracteres} caracteres, 1 número, 1 letra y no puede tener espacios.")
        return
    usuario = {
        "nombre": nombre,
        "sexo": sexo,
        "contraseña": contrasena
    }
    lista.append(usuario)
    print("Usuario ingresado exitosamente.\n")
def validar_contrasena(contrasena):
    if len(contrasena) < minimo_caracteres:
        return False
    if ' ' in contrasena:
        return False
    if not any(c.isalpha() for c in contrasena):
        return False
    if not any(c.isdigit() for c in contrasena):
        return False
    return True

def buscar_usuario(lista):
    nombre_buscar = input("Ingrese nombre del usuario a buscar: ").strip().lower()
    for usuario in lista:
        if usuario["nombre"].lower() == nombre_buscar:
            print("Usuario encontrado:")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Sexo: {usuario['sexo']}")
            print(f"Contraseña: {usuario['contraseña']}")
            return
    print("Usuario no encontrado.")

def eliminar_usuario(lista):
    usuario_eliminar = input("Ingrese nombre de usuario a eliminar: ").strip().lower()
    for i, usuario in enumerate(lista):
        if usuario['nombre'].lower() == usuario_eliminar:
            del lista[i]
            print("Usuario eliminado correctamente.\n")
            return
    print("Usuario no encontrado.")

def menu():
    while True:
        print("++++ Menu ++++")
        print("1) Ingresar usuario")
        print("2) Buscar usuario")
        print("3) Eliminar usuario")
        print("4) Salir")
        try:
            opcion = int(input("Ingrese opcion: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            registrar_usuario(lista)
        elif opcion == 2:
            buscar_usuario(lista)
        elif opcion == 3:
            eliminar_usuario(lista)
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida.")

menu()
