rango = range(1,11)

for numero in rango:
    print(numero)
    
nombre = "Daniel"

for letra in nombre:
    print(letra)
    
with open("titulos.txt") as archivo:
    for linea in archivo:
        print(linea)