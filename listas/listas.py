# numeros = "100001445,65465151,481,5151,48451"
# listaDeNumeros = [100001445,65465151,481,5151,4851]
calificacionesTallerPython = []
contador = 0
while contador <14:
    calificacion= float(input("Ingresa la primera calificacion: "))
    calificacionesTallerPython.append(calificacion)
    contador+=1
print(calificacionesTallerPython)
suma = 0
for calificacion in calificacionesTallerPython:
    suma = suma + calificacion
promedio = suma / len(calificacionesTallerPython)
print(promedio)