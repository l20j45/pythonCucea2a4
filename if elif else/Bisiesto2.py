Year ="0"
Residuo="0"
ResiduoYear="0"

Year = int(input("Ingrese el año a determinar: "))

Residuo = Year % 4
ResiduoYear = Year % 100

if Residuo == 0 and ResiduoYear==0:
    print("No es bisiesto")
elif Residuo == 0 and ResiduoYear!=0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
    
print(float(ResiduoYear)," ",float(Residuo))