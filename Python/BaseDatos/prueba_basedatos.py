import psycopg2

try:
    conexion = psycopg2.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',         # Conectarse a la base de datos
                                port='5432',
                                database='test_db')

    # .cursor() permite ejecutar sentencias en la base de datos, se almacena en una variable para poder llamarlo
    cursor = conexion.cursor()
    sql = 'SELECT * FROM persona'  # Sentencia
    cursor.execute(sql)  # Ejecuta la sentencia en la base de datos
    # Muestra la info que da la sentencia anteriormente ejecutada, se almacena en una variable tambien
    registros = cursor.fetchall()

    print(registros)
    cursor.close()                 # Hay que cerrar cursor
    conexion.close()               # Y la conexion tambien
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')
