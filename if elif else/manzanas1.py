descuento = 0

cantidadDeManzanas= float(input("Ingresa cuantas manzanas vas a vender"))
precioDeLasManzanas= float(input("Ingresa el precio de las manzanas"))

if cantidadDeManzanas == 18 :
    descuento = (cantidadDeManzanas * precioDeLasManzanas) *.15
    print(f"el descuento es de {descuento}")
elif cantidadDeManzanas >= 10 :
    descuento = (cantidadDeManzanas * precioDeLasManzanas) *.10
    print(f"el descuento es de {descuento}")
else:
    print("gracias por comprar")
totalAPagar = (cantidadDeManzanas * precioDeLasManzanas) - descuento

print(f"Total a pagar {totalAPagar} " )

