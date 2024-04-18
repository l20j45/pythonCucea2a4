import usuarioControlador
import usuarioModelo 

modeloUsuario = usuarioModelo.usuario
datos = usuarioControlador.consultarDatosUsuario()
# print(datos)
# [(1, 'Bruce', 'Diaz', ' ', 'soybatman', 'batman@gmail.com', '6666666'), (2, 'Clark', 'KENT', ' ', 'soysuperman', 'superman@gmail.com', '666'), (3, 'Barry', 'Allen', '', 'soyflash', 'flash@gmail.com', '66667882')]
for fila in datos:
    modeloUsuario['nombre'] = '@'+fila[1]
    modeloUsuario['apellidoPaterno'] = fila[2]
    modeloUsuario['apellidoMaterno'] = fila[3]
    print(modeloUsuario['nombre'] ,"Apellidos:", modeloUsuario['apellidoPaterno'] , modeloUsuario['apellidoMaterno'])