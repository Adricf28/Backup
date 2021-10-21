import psycopg2 as db

try:
    conexion = db.connect(user='postgres',
                                password='admin',
                                host='127.0.0.1',
                                port='5432',
                                database='test_db')

    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = (
        ('Kike', 'Montilla', 'kikemontilla@gmail.com'),
        ('Yoni', 'Gutierrez', 'yonigutierrez@gmail.com'),   # Se crea una tupla de tuplas para insertar varios
        ('Sisisi', 'Kemekeosincome', 'sisisikemekeosincome@gmail.com')
    )
    cursor.executemany(sentencia, valores)  # .executemany() para ejecutar varios registros
    conexion.commit()  
    registros_insertados = cursor.rowcount 
    print(f'Registros insertados: {registros_insertados}')
    cursor.close()
    conexion.close()
except Exception as error:
    print(f'Ha ocurrido el siguiente error: {error}')