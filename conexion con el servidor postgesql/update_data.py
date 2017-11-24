"""
Autor: Alfredo
"""

#Importamos la libreria psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el metodo config del modulo config
from config import config


def update_vendor(vendor_id, vendor_name):
    """ Actualización de venderores basados en vendor_id"""
	#Creamos la sentencia de actualización
    sql = """UPDATE vendors
                set vendor_name = %s
                WHERE  vendor_id = %s"""
	# Abrimos una sección para el control de exepciones
    try:
		#Inicializamos las variables
        connection = None
        updated_rows = 0
		# Leemos la configuracion de la base de datos
        params = config()
		# Conectamos a la base de datos
        connection = psycopg2.connect(**params)
		# Creamos un nuevo cursor
        cursor = connection.cursor()
        cursor.execute(sql, (vendor_name, vendor_id))
        updated_rows = cursor.rowcount
		# Aplicamos los cambios
        connection.commit()
        cursor.close()
		# Manejamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
		# Imprimimos el error resultante
        print(error)
    finally:
		# Verificamos que la conexion este cerrada, de lo contrario la cerramos
        if connection is not None:
            connection.close()
    return updated_rows


if __name__ == '__main__':
    print(update_vendor(1, '3M Corp'))
