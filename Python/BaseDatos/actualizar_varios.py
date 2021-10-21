import psycopg2 as db

try:
    conexion = db.connect(user='postgres',
                          password='admin',
                          host='127.0.0.1',
                          port='5432',
                          database='test_db')

    cursor = conexion.cursor()
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = (
        ('Aitorrr', 'Meeenta', 'aitormenta@gmail.com', 17),
        ('Adri', 'Ceniza', 'adriceniza@gmail.com', 6),
        ('Perro', 'Viejo', 'perrovieho@gmail.com', 2)
    )
    cursor.executemany(sentencia, valores)
    conexion.commit()
    registros_actualizados = cursor.rowcount
    print(f'Registros actualizados: {registros_actualizados}')
    cursor.close()
    conexion.close()
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')
