"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config

def insert_vendor(vendor_name):
    """Inserta un vendor dentro de la tabla de los vendores"""
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s) RETURNING vendor_id;"""
    #Inicializamos las variables a utilizar
	connection = None
    vendor_id = None
	# Intentamos el codigo
    try:
        # Asignamos los parametros de conexión
        params = config()
        # Conectamos a la base de datos y creamos un nuevo cursor
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        # Ejecutamos la sentencia y almacenamos el vendor_id
        cursor.execute(sql, (vendor_name,))
        vendor_id = cursor.fetchone()[0]
		# Realizamos los cambios
        connection.commit()
		# Cerramos la conexión
        cursor.close()
	# Atrapamos las exepciones
    except(Exception, psycopg2. DatabaseError) as error:
		 # Imprimimos las exepciones
        print(error)
    finally:
		# Cerramos la conexión
        if connection is not None:
            connection.close()
	#Retornamos id del vendedor
    return vendor_id


def insert_vendor_list(vendor_list):
    """Insertar varios vendores dentro de la tablas vendor"""
	# Creamos la sentencia SQL
    sql = """INSERT INTO vendors(vendor_name) VALUES(%s)"""
	# Inicializamos la variable de conexión
    connection = None
    # Intentamos el codigo
	try:
        # Asignamos los parametros de conexión
        params = config()
		# Conectamos a la base de datos y creamos un nuevo cursor
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
		# Ejecutamos la sentencia y realizamos los cambios
        cursor.executemany(sql, vendor_list)
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


if __name__ == '__main__':
    # Insertamos los vendedores
    insert_vendor_list([('AKM Semiconductor Inc',),
                   ('Asahi Glass Go. Ltd.',),
                   ('Aiking International Inc.',),
                   ('Dynacast International Inc.',),
                   ('Foster Electric Co. Ltd',),
                   ('Maruta Manufacturing Co. Ltd.',)])
