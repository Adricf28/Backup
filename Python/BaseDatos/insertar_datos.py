import psycopg2 as db

try:
    conexion = db.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',
                                port='5432',
                                database='test_db')

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Wanillo', 'Kokunero', 'wanillokokunero@gmail.com')
    cursor.execute(sentencia, valores)
    conexion.commit()  # .commit() hace que la informacion introducida se guarde en la base de datos
    registros_insertados = cursor.rowcount # .rowcount te dice cuantos registros se han insertado
    print(f'Registros insertados: {registros_insertados}')
    cursor.close()
    conexion.close()
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')