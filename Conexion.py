import sqlite3
from sqlite3 import Error

def conectar():
    try: 
        conexion = sqlite3.connect('data_base.db')
        return conexion
    except Error as err:
        print('Ocurrio un error al conectar, ')

def crearTabla(conexion):
    cursor = conexion.cursor()
    sql_1 = '''CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        nombre TEXT NOT NULL ,
        apellido TEXT NOT NULL ,
        clave_maestra TEXT NOT NULL
    )'''
    sql_2 = '''CREATE TABLE IF NOT EXISTS claves (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        nombre TEXT NOT NULL ,
        url_clave TEXT NOT NULL ,
        nombre_usuario TEXT NOT NULL ,
        clave TEXT NOT NULL ,
        descripcion TEXT
    )'''
    cursor.execute(sql_1)
    cursor.execute(sql_2)
    conexion.commit()
    conexion.close()

