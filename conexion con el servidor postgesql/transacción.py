"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config

def add_part(part_name, vendor_list):
    """Inserción se datos en la tabla parts"""
	
	# Creamos la sentencias de inserción
    insert_part = """INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id"""
    assign_vendor = """INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"""
	
	#Inicializamos la variable de conexión
    connection = None
	
	# Intentamos el codigo
    try:
		
		# Asignamos los parametros de conexión
        params = config()
		
		# Conectamos a la base de datos y creamos un nuevo cursor
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
		
        # Insertamos una nueva parte y obtenemos el id insertado
        cursor.execute(insert_part, (part_name,))
        part_id = cursor.fetchone()[0]
		
        # Asignamos las partes proveidas por los vendores
        for vendor_id in vendor_list:
            cursor.execute(assign_vendor, (vendor_id, part_id))
        
		# Realizamos los cambios
        connection.commit()
		
	# Atrapamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
		# Imprimimos las exepciones
        print(error)
    finally:
		# Cerramos la conexión
        if connection is not None:
            connection.close()


if __name__ == '__main__':
	# Insertamos datos en la tabla
    add_part('SIM Tray', (1, 2))
    add_part('Speaker', (3, 4))
    add_part('Vibrator', (5, 6))
    add_part('Antenna', (6, 4))
    add_part('Home Button', (1, 5))
    add_part('LTE Modem', (1, 5))