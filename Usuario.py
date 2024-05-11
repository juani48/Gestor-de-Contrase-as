import hashlib
from Conexion import *

def comprobarUsuario():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = 'SELECT * FROM usuario'
    cursor.execute(sql)
    usuario = cursor.fetchall()
    conexion.close()
    return usuario

def registrarUsuario(nombre, apellido, clave_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = '''INSERT INTO usuario (nombre,apellido,clave_maestra)
        VALUES (?,?,?)'''
        cm_cifrada = hashlib.sha256(clave_maestra.encode('utf-8')).hexdigest()
        datos = (nombre, apellido, cm_cifrada)
        cursor.execute(sql,datos)
        conexion.commit()
        conexion.close()
        return 'Registro correcto'
    except Error as err:
        return'Ocurrio un error durante el registro '+ str(arr)
    
def comprobarClave(id,clave_maestra):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = 'SELECT * FROM usuario WHERE id=? AND clave_maestra=?'
        cm_cifrada = hashlib.sha256(clave_maestra.encode('utf-8')).hexdigest()
        cursor.execute(sql,(id,cm_cifrada))
        datos = cursor.fetchall()
        conexion.close()
        return datos
    except Error as err:
        print('Ocurrio un error durante el registro '+ str(arr))


