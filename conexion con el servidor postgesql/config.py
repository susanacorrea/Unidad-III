"""
Autor: Susy
"""
#Importamos la libreria ConfigParser
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    # Creamos el parser
    parser = ConfigParser()
    # Analizacmos los parametros del archivo
    parser.read(filename)

    # Inicilizamos un diccionario
    db = {}
    # Obtenemos la section de postgreSQL
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        # Imprimimos errores emergentes
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    # Devolvemos el diccionario con los datos
    return db