import logging as log


log.basicConfig(level=log.INFO,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_dato.log'),
                    log.StreamHandler()
                ]) #muestra todos

if __name__ == '__main__':
    log.debug('Mensaje a nivel de debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel de critical')