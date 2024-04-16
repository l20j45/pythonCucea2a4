Estudiante = {
    "nombre": "daniel",
    "grado": "8",
    "carrera": "LTIN",
    "promedio": 8.9,
    }
Estudiante.update({"promedio": 100}) 
Estudiante["eSTallerista"] ="si"
Estudiante.pop("carrera")

print(Estudiante)
print(Estudiante.values())
print(Estudiante.keys())
print(Estudiante["promedio"])
print(Estudiante)
for valor in Estudiante:
    print(valor)

for valor in Estudiante.values():
    print(valor)