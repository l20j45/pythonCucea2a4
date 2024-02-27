nombre = 'Raul' #Contexto Global
def saludo():#Contexto Local
    print(nombre)
    print("Buen dia")

saludo()
saludo()
nombre = 'Xochitl'
saludo()
saludo()
