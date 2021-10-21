import psycopg2 as db

conexion = db.connect(user='postgres',
                            password='admin',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db')
try:
    #conexion.autocommit = True  # .autocommit hace que todos los cambios se guarden automaticamente
    cursor = conexion.cursor()
    
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    valores = ('Wanillo', 'Kokunero', 'wanillokokunero@gmail.com')
    cursor.execute(sentencia, valores)
    
    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Aitor', 'Menta', 'aitormenta@gmail.com', 17)
    cursor.execute(sentencia, valores)
    
    conexion.commit()  
except Exception as error:
    conexion.rollback() # .rollback da marcha atras en todos los cambios que se iban a ejecutar en caso de que haya un fallo
    print(f'Ha ocurrido un error con la transaccion: {error}')
finally:
    cursor.close()
    conexion.close()