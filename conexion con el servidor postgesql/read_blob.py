"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config

def read_blob(part_id, path_to_dir):
    """ Lector de archivos BLOB de una tabla """
	#Inicializamos la variable de conexión
    conn = None
	# Intentamos el codigo
    try:
        # Asignamos los parametros de conexión
        params = config()
        
		# Conectamos a la base de datos y creamos un nuevo cursor
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
		# Creamos la sentecia de selección
        cur.execute(""" SELECT part_name, file_extension, drawing_data
                        FROM part_drawings
                        INNER JOIN parts on parts.part_id = part_drawings.part_id
                        WHERE parts.part_id = %s """,
                    (part_id,))
		
		#obtenemos todas las tuplas 
        blob = cur.fetchone()
		
		# Abrimos el archivo
        open(path_to_dir + blob[0] + '.' + blob[1], 'wb').write(blob[2])
        
		#Cerramos la conexión
        cur.close()
		
	# Atrapamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		
		# Imprimimos las exepciones
        print(error)
    finally:
		# Cerramos la conexión
        if conn is not None:
            conn.close()