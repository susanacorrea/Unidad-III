"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config

def get_parts(vendor_id):
    """Muestra las partes proveidas por un vendedor especificado por el vendor_id """
	
	#Inicializamos la variable de conexión
    conn = None
	
	# Intentamos el codigo
    try:
        # Asignamos los parametros de conexión
        params = config()
        
		# Conectamos a la base de datos y creamos un nuevo cursor
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
		
		# Creamos la sentencia de selección y creamos un lista con la información
        cur.callproc('get_parts_by_vendor', (vendor_id,))
        row = cur.fetchone()
		
		# Mostramos las tuplas encontradas
        while row is not None:
            print(row)
            row = cur.fetchone()
        
		# Cerramos la conexión
        cur.close()
	
	# Atrapamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		# Imprimimos las exepciones
        print(error)
    finally:
		# Cerramos la conexión
        if conn is not None:
            conn.close()


if __name__ == '__main__':
	# Obtenemos los datos de la id número 1
    get_parts(1)