"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config


def get_vendors():
    """ Obtiene los datos de la tabla vendors"""
	
	#Inicializamos la variable de conexión
    conn = None
	
	# Intentamos el codigo
    try:
		# Asignamos los parametros de conexión
        params = config()
		
		# Conectamos a la base de datos y creamos un nuevo cursor
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
		
		# Ejecutamos la sentencia e imprimimos el numero de filas obtenidas
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
		
		# Enlistamos las filas y las imprimimos
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
		
		#Cerramos la conexión
        cur.close()
	
	# Atrapamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		# Imprimimos los errores resultantes
        print(error)
    finally:
		#Cerramos la conexión
        if conn is not None:
            conn.close()

def get_parts():
    """ Obtiene parts de la tabla parts """
    conn = None
	# Intentamos el codigo
    try:
		# Asignamos los parametros de conexión
        params = config()
		
		# Conectamos a la base de datos y creamos un nuevo cursor
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
		
		# Ejecutamos la sentencia y enlistamos los resultados
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
		
		# Imprimimos el numero de filas obtenidas
        print("The number of parts: ", cur.rowcount)
		
		# Imprimimos las tuplas obtenidas
        for row in rows:
            print(row)
		
		# Cerramos la conexión
        cur.close()
		
	# Atrapamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		# Imprimimos los errores resultantes
        print(error)
    finally:
		#Cerramos la conexión
        if conn is not None:
            conn.close()


if __name__ == '__main__':
	# Obtenemos los vendedores de la tabla vendedors
    get_vendors()
	# Obtenemos las partes de la tabla parts
    get_parts()
	