"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config


def update_vendor(vendor_id, vendor_name):
    """ Modifica los vendedores a través del vendor_id"""
	
	#Creamos la sentencia de actualización
    sql = """UPDATE vendors
                set vendor_name = %s
                WHERE  vendor_id = %s"""
	
	# Intentamos el codigo
    try:
		#Inicializamos las variables
        connection = None
        updated_rows = 0
		
		# Asignamos los parametros de conexión
        params = config()
		
		# Conectamos a la base de datos y creamos un nuevo cursor
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        
		#Ejecutamos la sentencia sql con el nombre del vendedor y su id
		cursor.execute(sql, (vendor_name, vendor_id))
		
		# Almacenamos el número de filas
        updated_rows = cursor.rowcount
		
		# Realizamos los cambios
        connection.commit()
        
		# Cerramos la conexión
		cursor.close()
		# Atrapamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
		# Imprimimos las exepciones
        print(error)
    finally:
		# Cerramos la conexión
        if connection is not None:
            connection.close()
	#Retornamos el número de tuplas modificadas
    return updated_rows


if __name__ == '__main__':
	#Modificamos el valor del vendedor con el id 1
    print(update_vendor(1, '3M Corp'))
