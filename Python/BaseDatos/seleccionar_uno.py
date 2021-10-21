import psycopg2 as db

try:
    conexion = db.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',
                                port='5432',
                                database='test_db')

    cursor = conexion.cursor()
    sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
    # id_persona = 2
    id_persona = input('Proporciona la pk a buscar: ') # pk = primary key
    llave_primaria = (id_persona,)  # La llave primaria debe ser una tupla siempre, y despues de la tupla hay que poner una coma para que reconozca que lo es
    cursor.execute(sentencia, llave_primaria) 
    registros = cursor.fetchone() # .fetchone() devuelve solo un registro

    print(registros)
    cursor.close()
    conexion.close()
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')
