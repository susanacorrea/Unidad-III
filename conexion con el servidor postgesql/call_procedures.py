"""
Autor: Alfredo
"""

#Importamos la librería psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config

#Creamos una función para mostrar venderores por id
def get_parts(vendor_id):
    """ Obtiene partes preveidas por un vendedor especificado por el vendor_id """
	#Inicializamos la variable de conexión
    conn = None
	# Abrimos una sección para el control de exepciones
    try:
        # Leemos la configuración de la base de datos
        params = config()
        # Conectamos a la base de datos
        conn = psycopg2.connect(**params)
        # Creamos un nuevo cursor
        cur = conn.cursor()
        # Otra sentencia que podria ser utlizada para la sección
        # cur.execute("SELECT * FROM get_parts_by_vendor( %s); ",(vendor_id,))
		# Creamos la sentencia de selección
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        # Creamos un set de la información
        row = cur.fetchone()
		# Mostramos las tuplas encontradas
        while row is not None:
            print(row)
            row = cur.fetchone()
        # Cerramos la conexión
        cur.close()
	# Manejamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		# Imprimimos el error resultante
        print(error)
    finally:
		# Verificamos que la conexión este cerrada, de lo contrario la cerramos
        if conn is not None:
            conn.close()


if __name__ == '__main__':
	# Obtenemos los datos de la id #1
    get_parts(1)