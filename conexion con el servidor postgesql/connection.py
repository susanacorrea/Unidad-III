"""
Autor: Alfredo
"""

#Importamos la librería psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2}
#Importamos el método config del modulo config
from config import config

#Creamos una función de conexión
def connect():
    """ Conexión con la base de datos del servidor de PostgreSQL """
    conn = None
    try:
        #Leemos los parametros de la conexión
        params = config()

        # Conectamos al servidor PostgreSQL
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # Creamos un nuevo cursor
        cur = conn.cursor()

        # Obtnemos la versión de la base de datos de PostgreSQL
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # Mostramos la versión de la base de datos de PostgreSQL
        db_version = cur.fetchone()
        print(db_version)

        # Cerramos la conexión con el servidor
        cur.close()
	# Manejamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
		#Imprmimimos los errores resultantes
        print(error)
		#verificamos que la conexión se haya cerrago, de lo contrario la cerramos
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
	#Ejecutamos la función
    connect()