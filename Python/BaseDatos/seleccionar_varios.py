import psycopg2 as db

try:
    conexion = db.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',
                                port='5432',
                                database='test_db')

    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'  # IN permite que selecciones todos los campos donde id_persona contenga los valores que le demos
    entrada = input('Proporciona las pk a buscar(separadas por comas): ')
    tupla = tuple(entrada.split(',')) # Split quita las comas, para que al crear la tupla se cree solo de los valores en sí, sin las comas
    print(tupla)
    llaves_primarias = (tupla,)  # Para meter varios valores hay que crear una tupla de tuplas
    cursor.execute(sentencia, llaves_primarias)
    registros = cursor.fetchall() 
    for i in registros:
        print(i)
    cursor.close()
    conexion.close()
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')
