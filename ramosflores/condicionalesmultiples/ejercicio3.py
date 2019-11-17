import os
# boleta de ventas de un restaurante
# declaracion de variables
cliente,precio_arroz,cantidad_arroz,precio_ceviche,cantidad_ceviche="",0.0,0,0.0,0
# imput
cliente=os.sys.argv[1]
precio_arroz=float(os.sys.argv[2])
cantidad_arroz=int(os.sys.argv[3])
precio_ceviche=float(os.sys.argv[4])
cantidad_ceviche=int(os.sys.argv[5])


# PROCESSING
total1=precio_arroz*cantidad_arroz
total2=precio_ceviche*cantidad_ceviche
monto_total=round(total2+total1)

# VERIFICADOR
comprador_compulsivo=(cantidad_arroz>5 and cantidad_ceviche>5)

# OUTPUT
print("########################")
print("# RESTAURANTE MECHITA  ")
print("#cliente:" , cliente)
print("# p.u de arroz:        " ,precio_arroz)
print("# platos de arroz      " , cantidad_arroz)
print ("# p.u de ceviche:     " ,precio_ceviche)
print ("# platos de ceviche:  " , cantidad_ceviche)
print ("# Monto total:        " , monto_total)

# Condicion Simple
# si el comprador es compulsivo, mostrarle que se ganaron un plato mas gratis
if (comprador_compulsivo==True):
    print ("GANASTE UN VALE DE UN PLATO MAS")

if(comprador_compulsivo<4):
    print("PUDISTE HABER GANADO UN PLATO MAS GRATIS,GRACIAS POR SU COMPRA ")
