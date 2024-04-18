from logger_base import log
from psycopg2 import pool
import sys
 
class ConecctionPool:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    
    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool
    
    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        log.debug(f'connection obtenida del pool: {connection} ')
        return connection
    
    @classmethod
    def connectionRelease(cls,connection):
        cls.getPool().putconn(connection)
        log.debug(f'Back the connection to the pool {connection}')
        
    @classmethod
    def connectionClosed(cls):
        cls.getPool().closeall()
        log.debug(f'all connection are closed')
        
if __name__ == '__main__':
    connection1 = ConecctionPool.getConnection()
    ConecctionPool.connectionRelease(connection1)
    connection2 = ConecctionPool.getConnection()
    