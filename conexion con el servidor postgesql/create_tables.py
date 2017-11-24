"""
Autor: Alfredo
"""

#Importamos la librería psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config

#Creamos un nuevo método para crear las tablas en la base de datos
def create_tables():

    """Creamos las tablas en la base de datos Postgresql"""

    commands= ("""CREATE TABLE log(
                  id SERIAL PRIMARY KEY,
                  ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                  phrase VARCHAR(128) NOT NULL,
                  letters VARCHAR(32) NOT NULL,
                  ip VARCHAR(16) NOT NULL,
                  browser_string VARCHAR(256) NOT NULL,
                  results VARCHAR(64) NOT NULL)""",

               """CREATE TABLE vendors(
                  vendor_id SERIAL PRIMARY KEY, 
                  vendor_name VARCHAR(255) NOT NULL)""",

               """CREATE TABLE parts(
                  part_id SERIAL PRIMARY KEY, 
                  part_name VARCHAR(255) NOT NULL)""",

               """CREATE TABLE part_drawings(
                  part_id INTEGER PRIMARY KEY, 
                  file_extension VARCHAR(5) NOT NULL, 
                  drawing_data BYTEA NOT NULL, 
                  FOREIGN KEY(part_id) REFERENCES parts(part_id) ON UPDATE CASCADE ON DELETE CASCADE)""",

                """CREATE TABLE vendor_parts( 
                  vendor_id INTEGER NOT NULL, 
                  part_id INTEGER NOT NULL, 
                  PRIMARY KEY(vendor_id, part_id), 
                  FOREIGN KEY(vendor_id) REFERENCES vendors(vendor_id) ON UPDATE CASCADE ON DELETE CASCADE,
                  FOREIGN KEY(part_id) REFERENCES parts(part_id) ON UPDATE CASCADE ON DELETE CASCADE)""")

    #Inicializamos la variable connention con el valor de None
    connection = None
    #Abrimos una sección para el control de exepciones
    try:
        #Asignamos el metodo config() a la variable params
        params = config()
        # Leemos los parametros de conexion
        connection = psycopg2.connect(**params)
        #Creamos un nuevo cursor
        cursor = connection.cursor()
        # Creamos la tabla una por una
        for command in commands:
            cursor.execute(command)
        # Cerramos la conexión con el servidor PostgresSQL
        cursor.close()
        #Aplicamos los cambios
        connection.commit()
        #Manejamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
        #Imprimimos el error resultante
        print(error)
    finally:
        #Verificamos que la conexión este cerrada, de lo contrario la cerramos
        if connection is not None:
            connection.close()

if __name__ == '__main__':
    #Ejecutamos la funcion creada
    create_tables()
