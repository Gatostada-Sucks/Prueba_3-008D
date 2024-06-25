import json

#Recuerda: ¨r¨ es por read, ¨w¨ es para escribir y ¨a¨ es para añadir al final del json.

def Agregar_Usuarios(UsuarioID:int, nombre:str, email:str, fecha_de_registro:str):
    with open ("biblioteca.json", mode = "r") as AgregarUsuario:
        LeerUsuario = json.load(AgregarUsuario)
#La gracia del Load, es para poder cargar los datos.
    Usuario = {
    "UsuarioID": len(LeerUsuario["Usuario"]) + 1,
    "Nombre": nombre,
    "Email": email,
    "fecharegistro": fecha_de_registro
    }
    LeerUsuario["Usuario"].append(Usuario)

    with open("biblioteca.json", mode = "w") as ReemplazarUsuario:
        json.dump(LeerUsuario, ReemplazarUsuario, indent = 4)
    
    print("Usuario agregado.")

def Editar_Usuarios(UsuarioID:int, nombre:str, email:str, fecha_de_registro:str):
    with open ("biblioteca.json", mode = "r") as EscribirUsuario:
        LeerUsuario = json.load(EscribirUsuario)
        Buscador = False
        for i in LeerUsuario["Usuario"]:
            if i["UsuarioID"] == UsuarioID:
                i["Nombre"] == nombre
                i["Email"] == email
                i["fecharegistro"] == fecha_de_registro
                Buscador = True
                break
            if not Buscador:
                    print("ID no encontrada.")
            else:
                with open ("biblioteca.json", mode = "w") as EscribirUsuario:
                    json.dump(LeerUsuario, EscribirUsuario, indent = 4)
                    print("Usuario actualizado.")

def Eliminar_Usuarios(UsuarioID:int):
    with open ("biblioteca.json", mode = "r") as EliminarUsuario:
        LeerUsuario = json.load(EliminarUsuario)
        Buscador = False
        for i in LeerUsuario["Usuario"]:
            if i["UsuarioID"] == UsuarioID:
                LeerUsuario["Usuario"].pop(i)
                Buscador = True
                break
            if not Buscador:
                    print("ID no encontrada.")
            else:
                    print("Usuario eliminado.")

def Buscar_Usuarios(UsuarioID:int):
    with open ("biblioteca.json", mode = "r") as BuscarUsuarios:
        LeerUsuario = json.load(BuscarUsuarios)
        Buscador = False
        for i in LeerUsuario["Usuario"]:
            if i["UsuarioID"] == UsuarioID:
                Buscador = True
        if not Buscador:
            print("La ID que está buscando no existe")
        else:
            print(LeerUsuario["Usuario"])