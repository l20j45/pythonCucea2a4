from UsuarioDao import *
import sys

def Menu():
    print("""1) Listar Usuarios
          2) Agregar Usuarios
          3) Actualizar usuarios
          4) Eliminar usuarios
          5) Salir""")

option = 1
while option !=5:
    Menu()
    option = int(input('Ingresa la opcion del menu: '))
    if option == 1:
        view_users()
    elif option==2:
        user=input("ingresa el usuario: ")
        password=input("ingresa el password: ")
        insertUser(user,password)
    elif option==3:
        iduser=input("ingresa el id del usuario: ")
        user=input("ingresa el usuario: ")
        password=input("ingresa el password: ")
        updateUser(iduser,user,password)
    elif option==4:
        iduser=input("ingresa el id del usuario: ")
        delUser(iduser)
    elif option==5:
        sys.exit()
