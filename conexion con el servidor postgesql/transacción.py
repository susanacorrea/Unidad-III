"""
Autor: Alfredo
"""

#Importamos la librería psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config

# Creamos una función para insertar datos en la tabla parts
def add_part(part_name, vendor_list):
    """Inserción se datos en la tabla parts"""
	# Creamos la sentencia de inserción en la tabla parts
    insert_part = """INSERT INTO parts(part_name) VALUES(%s) RETURNING part_id"""
    # Creamos la sentencia de inserción en la tabla vendors
    assign_vendor = """INSERT INTO vendor_parts(vendor_id, part_id) VALUES(%s, %s)"""
	#Inicializamos la variable de conexión
    connection = None
	# Abrimos una seccion para el control de exepciones
    try:
		# Leemos la configuración de la base de datos
        params = config()
		# Conectamos a la base de datos
        connection = psycopg2.connect(**params)
		# Creamos un nuevo cursor
        cursor = connection.cursor()
        # Insertamos una nueva parte
        cursor.execute(insert_part, (part_name,))
        # Obtenemos el id insertado
        part_id = cursor.fetchone()[0]
        # assign parts provided by vendors
        for vendor_id in vendor_list:
            cursor.execute(assign_vendor, (vendor_id, part_id))
        # Aplicamos los cambios
        connection.commit()
		# Manejamos las exepciones
    except(Exception, psycopg2.DatabaseError) as error:
		# Imprimimos el error resultante
        print(error)
    finally:
		# Verificamos que la conexion este cerrada, de lo contrario la cerramos
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