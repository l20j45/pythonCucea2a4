nombre = 'Raul' #Contexto Global
idioma = 'Aleman' #Contexto Global

def saludo(nombreFuncion,idioma):#Contexto Local
    # nombre = 'Xochitl'
    print(nombreFuncion)
    print(f"Buen dia en {idioma}" )
    # print(nombre)
    # print("Buen dia")
    print("=====================")

saludo(nombre,idioma)
saludo(nombre,'Aleman')
saludo('Felipe','Framces')

