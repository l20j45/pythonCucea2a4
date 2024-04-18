from logger_base import log

class Usuario():
    def __init__(self,idUsuario=None,username=None,password=None):
        self._idUsuario=idUsuario
        self._username=username
        self._password=password
        
    @property
    def idUsuario(self):
        return self._idUsuario
    
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,value):
        self._username = value
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,value):
        self._password = value
    
    def __str__(self):
        return f'Usuario: idUsuario={self._idUsuario}, username={self._username}, password={self._password}'
    
if __name__ == '__main__':
    usuario1 = Usuario(1,'admin', 'admin')
    log.debug(usuario1)
    usuario2 = Usuario(username='victor',password='victor')
    log.debug(usuario2)