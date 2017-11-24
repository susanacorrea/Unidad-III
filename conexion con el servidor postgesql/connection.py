"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config

def connect():
    """ Conexión con el servidor de PostgreSQL """
    # Creamos e inicializamos la variable de conexión
	conn = None
    try:
         # Asignamos los parametros de conexión
        params = config()

        # Conectamos al servidor
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # Creamos un cursor
        cur = conn.cursor()

        # Obtnemos la versión de PostgreSQL
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # Mostramos la versión de PostgreSQL
        db_version = cur.fetchone()
        print(db_version)

        # Cerramos la conexión
        cur.close()
	# Atrapamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
		# Imprimimos las exepciones
        print(error)
    finally:
		# Cerramos la conexión
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
	#Ejecutamos la conexión
    connect()