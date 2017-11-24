"""
Autor: Alfredo
"""

#Importamos la librería psycopg2, encargada de adaptar el lenguaje de Python a PostgreSQL
import psycopg2
#Importamos el método config del modulo config
from config import config

#Creamos una función para borrar un elemento a través de su id
def delete_part(part_id):
    """ Eliminar part por part_id """
    #Inicializamos la variable de conexión
    conn = None
    # Inicializamos la variable de rows_deleted
    rows_deleted = 0
    # Abrimos una sección para el control de exepciones
    try:
        # Leemos la configuración de la base de datos
        params = config()
        # Conectamos a la base de datos
        conn = psycopg2.connect(**params)
        # Creamos un nuevo cursor
        cur = conn.cursor()
        # Ejecutamos la sentencia con el parametro de la id
        cur.execute("DELETE FROM parts WHERE part_id = %s", (part_id,))
        # Obtenemos el número de tuplas afectadas
        rows_deleted = cur.rowcount
        # Aplicamos los cambios
        conn.commit()
        # Cerramos la conexión con la base de datos
        cur.close()
    # Manejamos las exepciones
    except (Exception, psycopg2.DatabaseError) as error:
        # Imprimimos el error resultante
        print(error)
    finally:
        # Verificamos que la conexión este cerrada, de lo contrario la cerramos
        if conn is not None:
            conn.close()
    #Retornamos el número de tuplas afectadas
    return rows_deleted


if __name__ == '__main__':
    #Ejecutamos la sentencia con el id 2, almacenando el valor retornado en una variable
    deleted_rows = delete_part(2)
    #Imprimimos el numero de tuplas afectadas
    print('The number of deleted rows: ', deleted_rows)