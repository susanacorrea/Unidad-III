"""
Autor: Alfredo
"""

#Importamos la libreria psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config


def write_blob(part_id, path_to_file, file_extension):
    """ Inserción una información en formato BLOB dentro de una tabla"""
	#Inicializamos la variable de conexión
    conn = None
	# Abrimos una sección para el control de exepciones
    try:
        # Leemos los datos de la imagen 
        drawing = open(path_to_file, 'rb').read()
        # Leemos la configuración de la base de datos
        params = config()
        # Conectamos a la base de datos
        conn = psycopg2.connect(**params)
        # Creamos un nuevo cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute("INSERT INTO part_drawings(part_id,file_extension,drawing_data) " +
                    "VALUES(%s,%s,%s)",
                    (part_id, file_extension, psycopg2.Binary(drawing)))
        # Aplicamos los cambios
        conn.commit()
        # close the communication with the PostgresQL database
        cur.close()
		# Manejamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
		# Imprimimos el error resultante
        print(error)
    finally:
		# Verificamos que la conexion este cerrada, de lo contrario la cerramos
        if conn is not None:
            conn.close()
			

if __name__ == '__main__':
	# Isertamos registros en la tabla
    write_blob(1, 'images/simtray.jpg', 'jpg')
    write_blob(2, 'images/speaker.jpg', 'jpg')