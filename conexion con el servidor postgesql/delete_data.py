"""
Autor: Susy
"""
#Importamos la librería psycopg2 y config (el archivo que hemos generado)
import psycopg2
from config import config


def delete_part(part_id):
    """ Eliminar part a través del part_id """
    
	#Inicializamos las variables a utilizar
    conn = None
    rows_deleted = 0
    
	# Intentamos el codigo
    try:
        
		# Asignamos los parametros de conexión
        params = config()
        
		# Conectamos a la base de datos y creamos un nuevo cursor
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
		# Ejecutamos la sentencia y almacenamos el número de tuplas afectadas
        cur.execute("DELETE FROM parts WHERE part_id = %s", (part_id,))
        rows_deleted = cur.rowcount
        
		# Realizamos los cambios
        conn.commit()
        
		# Cerramos la conexión
        cur.close()
    
	# Atrapamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
        
		# Imprimimos las exepciones
        print(error)
    finally:
        
		# Cerramos la conexión
        if conn is not None:
            conn.close()
    
	#Retornamos el número de tuplas eliminadas
    return rows_deleted


if __name__ == '__main__':
    #Eliminamos la tupla con el id 2
    deleted_rows = delete_part(2)
    
	#Imprimimos el numero de tuplas eliminadas
    print('The number of deleted rows: ', deleted_rows)