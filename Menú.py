from Biblioteca_Libro_Mundo import*
import time, os

menu = ("agregar_usuarios", "editar_usuarios", "eliminar_usuarios", "buscar_usuarios")
counter = 0
print("******************************")
print("* ¡BIENVENIDO A LIBRO MUNDO! *")
print("******************************")
time.sleep(3)
os.system("cls")
for i in menu:
    counter += 1
    print(f"[{counter}]:>{i}")

while True:
    opciones = int(input("Por favor elija la opción que desee hacer: "))

    if opciones == 1:
        nombre = str(input("Por favor ingrese el nombre a agregar: "))
        email = str(input("Por favor ingrese el email a agregar: "))
        fecha = str(input("Día, mes y año de registro (Escribir por favor con números): "))
        Agregar_Usuarios(nombre, email, fecha)
    elif opciones == 2:
        UserID = int(input("Por favor elija la ID del usuario que desee editar:"))
        nombre = str(input("Por favor ingrese el nuevo nombre: "))
        email = str(input("Por favor ingrese el nuevo email: "))
        fecha = str(input("Fecha de edición: "))
        Editar_Usuarios(UserID, nombre, email, fecha)
    elif opciones == 3:
        UserID = int(input("Ingrese la ID del usuario que desea eliminar: "))
        Eliminar_Usuarios(UserID)
    elif opciones == 4:
        UserID = int(input("Ingrese la ID del usuario que desea buscar: "))
        Buscar_Usuarios(UserID)
    else:
        print("¡Gracias por preferirnos!")
        time.sleep(3)
        break