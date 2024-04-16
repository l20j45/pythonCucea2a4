nombre = "Oscar"
nombre = input("Ingresa tu nombre: ")
for letra in nombre:
    print(letra)
    
print(nombre.upper())
print(nombre.lower())
print(nombre[0])
print(nombre[2])
print(nombre[::-1])
print(nombre.replace('s','a'))
print(nombre.split("a"))
print(nombre[0:4])