"""
Autor: Alfredo
"""

#Importamos la librería psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config

#Creamos una función para leer las imagenes
def read_blob(part_id, path_to_dir):
    """ Lector de información en formato BLOB desde una tabla """
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
        # execute the SELECT statement
        cur.execute(""" SELECT part_name, file_extension, drawing_data
                        FROM part_drawings
                        INNER JOIN parts on parts.part_id = part_drawings.part_id
                        WHERE parts.part_id = %s """,
                    (part_id,))

        blob = cur.fetchone()
        open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])
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