import psycopg2 as db

try:
    conexion = db.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',
                                port='5432',
                                database='test_db')

    cursor = conexion.cursor()
    sentencia = 'DELETE FROM persona WHERE id_persona = %s'
    entrada = (input('Selecciona el valor a eliminar: '))
    valores = (entrada,)
    cursor.execute(sentencia, valores)  
    conexion.commit()  
    registros_eliminados = cursor.rowcount 
    print(f'Registros eliminados: {registros_eliminados}')
    cursor.close()
    conexion.close()
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')