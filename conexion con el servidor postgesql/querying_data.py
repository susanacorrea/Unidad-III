"""
Autor: Alfredo
"""

#Importamos la libreria psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config


def get_vendors():
    """ query data from the vendors table """
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
		#Ejecutamos la sentencia de selección
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
		#Imprimimos el numero total de tuplas encontradas
        print("The number of parts: ", cur.rowcount)
		#Asiganamos a una variable los valores de las tuplas encontradas
        row = cur.fetchone()
		#Imprimimos todas las tuplas que encuentre
        while row is not None:
            print(row)
            row = cur.fetchone()
		#Cerramos la conexión
        cur.close()
	# Manejamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		# Imprimimos los errores resultantes
        print(error)
    finally:
		# Verificamos que la conexión este cerrada, de lo contrario la cerramos
        if conn is not None:
            conn.close()

#Creamos una función para obtener las partes
def get_parts():
    """ Obtiene parts de la tabla parts """
    conn = None
    try:
        params = config()
		# Conectamos a la base de datos
        conn = psycopg2.connect(**params)
		# Creamos un nuevo cursor
        cur = conn.cursor()
		# Ejecutamos la sentencia se sección
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
		#Almacenamos todas las tuplas resultantes
        rows = cur.fetchall()
		#Imprimimos el número total de tuplas arrojadas
        print("The number of parts: ", cur.rowcount)
		#Imprimimos las tuplas obtenidas
        for row in rows:
            print(row)
		#Cerramos la conexión
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
	#Obtenemos los vendedores
    get_vendors()
	#Imprimira lo siguiente
    (1, '3M Corp')
    (2, 'AKM Semiconductor Inc.')
    (3, 'Asahi Glass Co Ltd.')
    (4, 'Daikin Industries Ltd.')
    (5, 'Dynacast International Inc.')
    (6, 'Foster Electric Co. Ltd.')
    (7, 'Murata Manufacturing Co. Ltd.')
	#Obtenemos las partes
    get_parts()
	#Imprimira lo siguiente
    (4, 'Antenna')
    (5, 'Home Button')
    (6, 'LTE Modem')
    (1, 'SIM Tray')
    (2, 'Speaker')
    (3, 'Vibrator')