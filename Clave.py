from Conexion import *

def registrar(nombre, url, nombre_usuario, clave, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = '''INSERT INTO claves (
            nombre, url_clave, nombre_usuario, clave, descripcion)
            VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(sql, (nombre, url, nombre_usuario, clave, descripcion))
        conexion.commit()
        conexion.close()
        return 'Registro correcto'
    except Error as err:
        return 'Ocurrio un error' + str(err)

def mostrar():
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = '''SELECT * FROM claves'''
        cursor.execute(sql)
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        return 'Ocurrio un error' + str(err)
    return datos

def buscar(id):
    datos = []
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = '''SELECT * FROM claves WHERE id=?'''
        cursor.execute(sql,(id,))
        datos = cursor.fetchall()
        conexion.close()
    except Error as err:
        return 'Ocurrio un error' + str(err)
    return datos

def modificar(id,nombre, url, nombre_usuario, clave, descripcion):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = '''UPDATE claves 
        SET nombre=?, url_clave=?, nombre_usuario=?, clave=?, descripcion=?
        WHERE id=?'''
        datos = (nombre, url, nombre_usuario, clave, descripcion, id)
        cursor.execute(sql,datos)
        conexion.commit()
        conecxion.close()
        return 'Se mmodifico la informacion'
    except Error as err:
        return 'Ocurrio un error' + str(err)

def eliminar(id):
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        sql = '''DELETE FROM claves WHERE id=?'''
        cursor.execute(sql,(id,))
        conexion.commit()
        conexion.close()
        return 'Se elimino la infomracion'
    except Error as err:
        return 'Ocurrio un error' + str(err)

