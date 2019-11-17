import os
# boleta de ventas de una tienda de ropa y zapatillas
# declaracion de variables
cliente,precio_zapatillas,cantidad_zapatillas,precio_polera,cantidad_polera="",0.0,0,0.0,0
# imput
cliente=os.sys.argv[1]
precio_zapatillas=float(os.sys.argv[2])
cantidad_zapatillas=int(os.sys.argv[3])
precio_polera=float(os.sys.argv[4])
cantidad_polera=int(os.sys.argv[5])


# PROCESSING
total1=precio_zapatillas*cantidad_zapatillas
total2=precio_polera*cantidad_polera
monto_total=round(total2+total1)

# VERIFICADOR
comprador_compulsivo=(monto_total>=1000)

# OUTPUT
print("########################")
print("# RESTAURANTE MECHITA  ")
print("#cliente:" , cliente)
print("# p.u de zapatillas:         " ,precio_zapatillas)
print("# cantidad de zapatillas:    " , cantidad_zapatillas)
print ("# p.u de poleras:           " ,precio_polera)
print ("# cantidad de poleras:        " , cantidad_polera)
print ("# Monto total:              " , monto_total)

# Condicion Simple
# si el comprador es compulsivo, decirle que puede llevarse un articulo completamente gratis
if (comprador_compulsivo==True):
    print ("GANASTE UN ARTICULO POR SUPERAR LOS 1000 SOLES DE COMPRA")
else:
    print("NO PUDO GANARSE EL ARTICULO ADICIONAL")
