import mysql.connector
from mysql.connector import Error

def consultarDatosUsuarios():
    try:
        connection = mysql.connector.connect(host='148.202.39.38',
                                            database='bolicesupreme',
                                            user='test',
                                            password='test')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM usuario")
            record = cursor.fetchall()
            return record
            # modeloUsuario = usuarioModelo.usuario
            # for row in record:
            #     modeloUsuario['nombre'] ='@'+row[1]
            #     print(modeloUsuario['nombre'])
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
