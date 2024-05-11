import os
from getpass import getpass
from Conexion import *
from Usuario import *
from Clave import *
conexion = conectar()
crearTabla(conexion)

def inicio():
    os.system('cls')
    #si no existe un usuario
    if len(comprobarUsuario()) == 0:
        print('Bienvenido, registre su infomracion')
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su apellido: ')
        clave_maestra = getpass('Ingrese su contraseña: ')
        ok = registrarUsuario(nombre,apellido,clave_maestra)
        if(ok == 'Registro correcto'):
            print(f'{ok} \nBienvenido {nombre}')
            menu()
        else:
            print(ok)
    #si ya se registro
    else:
        clave_maestra = getpass('Ingrese su contraseña: ')
        ok = comprobarClave(1,clave_maestra)
        if len(ok) == 0:
            print('Contraseña incorrecta')
        else:
            print('Contraseña correcta, bienvenido')
            menu()

def menu():
    while True:
        print('Seleccione una de las siguiente opciones: ')
        print('\t1- Añadir un registro de usuario')
        print('\t2- Ver todos los registros de usuario')
        print('\t3- Visualizar un registro de usuario')
        print('\t4- Modificar un registro de usuario')
        print('\t5- Eliminar un registro de usuario')
        print('\t6- Salir')
        num = input('Ingrese una opcion: ')
        #Añadir contraseña
        if num == '1':
            print("Añadiendo registro")
            nuevo_registro()
        #Ver todas las contraseñas
        elif num == '2':
            print("Visualizando registros")
            mostrar()
        #Visualizar una contraseña
        elif num == '3':
            print("Visualizando un registro")
            claveBuscar()
        #Modificar una contraseña
        elif num == '4':
            print("Modificando registro")
            modificarClave()
        #Eliminar una contraseña
        elif num == '5':
            print("Eliminado registro")
            eliminarClave()
        #Salir
        elif num == '6':
            break
        else:
            print('No ingreso una opcion valida')
        print('\n')

def nuevo_registro():
    nombre = input('Ingrese el nombre del lugar a registrar una usuario: ')
    url = input('Ingrese la url: ')
    nombre_usuario = input('Ingrese su nombre de usuario: ')
    clave = input('Ingrese la clave: ')
    descripcion = input('Ingrese alguna descripcion: ')
    ok = registrar(nombre, url, nombre_usuario, clave, descripcion)
    print(ok)

def claveBuscar():
    id = input('Ingrese el id a buscar: ')
    ok = buscar(id)
    print(ok)

def modificarClave():
    id = input('Ingrese un ID existente: ')
    nombre = input('Ingrese el nombre a modificar: ')
    url = input('Ingrese la url a modificar: ')
    nombre_usuario = input('Ingrese el nombre de usuario a modificar: ')
    clave = input('Ingrese la clave a modificar: ')
    descripcion = input('Ingrese alguna descripcion a modificar: ')
    ok = modificar(id,nombre, url, nombre_usuario, clave, descripcion)
    print(ok)

def eliminarClave():
    id = input('Ingrese un ID a eliminar: ')
    ok = eliminar(id)
    print(ok)

inicio()

