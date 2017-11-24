"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config


def write_blob(part_id, path_to_file, file_extension):
    """ Inserción de archivo BLOB dentro de una tabla"""
	
	#Inicializamos la variable de conexión
    conn = None
	
	# Intentamos el codigo
    try:
        # Leemos los datos de la imagen 
        drawing = open(path_to_file, 'rb').read()
        
		# Asignamos los parametros de conexión
        params = config()
        
		# Conectamos a la base de datos y creamos un nuevo cursor
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
		# Ejecutamos la sentencia de insercción
        cur.execute("INSERT INTO part_drawings(part_id,file_extension,drawing_data) " +
                    "VALUES(%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        
		# Realizamos los cambios
        conn.commit()
        
		#Cerramos la conexión
        cur.close()
		
	# Atrapamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		# Imprimimos las exepciones
        print(error)
    finally:
		#Cerramos la conexión
        if conn is not None:
            conn.close()
			

if __name__ == '__main__':
	# Isertamos imagenes en la tabla
    write_blob(1, 'images/simtray.jpg', 'jpg')
    write_blob(2, 'images/speaker.jpg', 'jpg')