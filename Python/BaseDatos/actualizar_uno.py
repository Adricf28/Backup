import psycopg2 as db

try:
    conexion = db.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',
                                port='5432',
                                database='test_db')

    cursor = conexion.cursor()
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Aitor', 'Menta', 'aitormenta@gmail.com', 17)
    cursor.execute(sentencia, valores)  
    conexion.commit()  
    registros_actualizados = cursor.rowcount 
    print(f'Registros actualizados: {registros_actualizados}')
    cursor.close()
    conexion.close()
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')