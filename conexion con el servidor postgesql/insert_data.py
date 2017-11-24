"""
Autor: Alfredo
"""

#Importamos la librería psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config

#Creamos una función para insertar valores en vendor
#Asignando como parametro vendor_name
def insert_vendor(vendor_name):
    """Insertamos un nuevo vendor dentro de la tabla vendors"""
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id;"""
    # Inicializamos la variable de conexión
    connection = None
    # Inicializamos la variable del vendor_id con el valor de None
    vendor_id = None
	# Abrimos una sección para el control de exepciones
    try:
        # Leemos la configuración de la base de datos
        params = config()
        # Conectamos a la base de datos
        connection = psycopg2.connect(**params)
        # Creamos un nuevo cursor
        cursor = connection.cursor()
        # Ejecutamos la sentencia de insercción
        cursor.execute(sql, (vendor_name,))
        # Obtenemos el id insertado
        vendor_id = cursor.fetchone()[0]
        # Aplicamos los cambios
        connection.commit()
		# Cerramos la conexión
        cursor.close()
	# Manejamos las exepciones
    except(Exception, psycopg2. DatabaseError) as error:
		# Imprimimos los errores resultantes
        print(error)
    finally:
		# Verificamos que la conexión este cerrada, de lo contrario la cerramos
        if connection is not None:
            connection.close()
	# Retornamos el valor de vendor_id
    return vendor_id

# Creamos una función para la inserción de venderores
def insert_vendor_list(vendor_list):
    """Insertar multiples vendors dentro de la tablas vendor"""
	# Creamos la sentencia SQL para la insercción
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
	# Inicializamos la variable de conexión
    connection = None
    try:
        # Leemos los parametros de conexión
        params = config()
		# Creamos la conexión
        connection = psycopg2.connect(**params)
        # Creamos un nuevo cursor
        cursor = connection.cursor()
		# Ejecutamos la sentencia
        cursor.executemany(sql, vendor_list)
        # Aplicamos los cambios
        connection.commit()
        # Cerramos la conexión
        cursor.close()
	# Manejamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
		# Imprimimos el error resultante
        print(error)
    finally:
		# Verificamos que la conexion este cerrada, de lo contrario la cerramos
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    # Insertamos los vendedores
    insert_vendor_list([('AKM Semiconductor Inc',),
                   ('Asahi Glass Go. Ltd.',),
                   ('Aiking International Inc.',),
                   ('Dynacast International Inc.',),
                   ('Foster Electric Co. Ltd',),
                   ('Maruta Manufacturing Co. Ltd.',)])
