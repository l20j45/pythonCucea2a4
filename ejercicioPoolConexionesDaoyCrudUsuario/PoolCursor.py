from logger_base import log
from ConecctionPool import ConecctionPool

class PoolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'__enter__() called')
        self._connection = ConecctionPool.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor
    
    def __exit__(self, exc_type, exc_value, traceback):
        log.debug(f'__exit__() called')
        if exc_value:
            self._connection.rollback()
            log.error(f'a exception occurred {exc_value} {exc_type} {traceback}')
        else:
            self._connection.commit()
            log.info(f'transacction commit')
        self._cursor.close()
        ConecctionPool.connectionRelease(self._connection)
            
if __name__ == '__main__':
    with PoolCursor() as cursor:
        log.debug(f'inside with block')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())