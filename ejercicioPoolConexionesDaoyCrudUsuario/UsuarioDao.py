from Usuario import Usuario
from PoolCursor import PoolCursor
from logger_base import log
import os

class UsuarioDao:
    
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _SELECCIONARESPECIFICO = 'SELECT * FROM usuario where id_usuario=%s ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES (%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario set username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
    
    @classmethod
    def selection(cls):
        with PoolCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registers = cursor.fetchall()
            usuarioList = []
            for register in registers:
                usuarioTemplate = Usuario(register[0], register[1], register[2])
                usuarioList.append(usuarioTemplate)
            return usuarioList
    
    @classmethod
    def specificSelection(cls, user):
        with PoolCursor() as cursor:
            valor = (user.idUsuario,)
            cursor.execute(cls._SELECCIONARESPECIFICO, valor)
            registers = cursor.fetchone()
            return registers
    
    @classmethod
    def Delete(cls,user):
        with PoolCursor() as cursor:
            userSearched = UsuarioDao.specificSelection(user)
            log.debug(f'Deleting user {userSearched}')  
            valor = (user.idUsuario,)
            cursor.execute(cls._ELIMINAR, valor)
            return cursor.rowcount                 
            
    @classmethod
    def Update(cls,user):
        with PoolCursor() as cursor:
            usuarioSearched = UsuarioDao.specificSelection(user)
            log.debug(f'Deleting user1 {usuarioSearched}')  
            valores = (user.username,user.password,user.idUsuario,)
            cursor.execute(cls._ACTUALIZAR, valores)
        usuarioSearched = UsuarioDao.specificSelection(user)
        log.debug(f'Deleting user2 {usuarioSearched}')    
        return cursor.rowcount  
    
    @classmethod
    def Insert(cls,user):
        with PoolCursor() as cursor:
            log.debug(f'Persona a insertar {user} ')
            valores = (user.username,user.password)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
            
def view_users():
    users = UsuarioDao.selection()
    for user in users:
        log.debug(user)
        
def view_user(id):
    user2 = Usuario(idUsuario=str(id))
    userfinder = UsuarioDao.specificSelection(user2)
    log.debug(userfinder)
    
def updateUser(iduser,username,password):
    user3 = Usuario(idUsuario=iduser,username=username,password=password)
    userDeleted = UsuarioDao.Update(user3) 
    log.debug(f'Persona a modificada {userDeleted}')
    
def delUser(idUsuario):
    user3 = Usuario(idUsuario=idUsuario)
    userDeleted = UsuarioDao.Delete(user3) 
    log.debug(f'Persona a borrada {userDeleted}')
    
def insertUser(username,password):
    user4 = Usuario(username=username,password=password)
    userInserted = UsuarioDao.Insert(user4) 
    log.debug(f'Persona a insertada {userInserted}')
    view_users()
    
if __name__ == '__main__':
    os.system ("cls")
    
"""     view_users()#ver todos
    view_user(5)#ver solo uno """
    
    
"""     user3 = Usuario(idUsuario='15')
    userDeleted = UsuarioDao.Delete(user3) 
    log.debug(f'Persona a borrada {userDeleted}') """ #borrado
    
