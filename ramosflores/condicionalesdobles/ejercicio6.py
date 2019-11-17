import os
# boleta de ventas
# declaracion de valores
cliente,fecha,hora,precio_producto,cantidad_producto="","","",0.0,0

#imput
cliente=os.sys.argv[1]
fecha=os.sys.argv[2]
hora=os.sys.argv[3]
precio_producto=float(os.sys.argv[4])
cantidad_producto=int(os.sys.argv[5])


# prosessing
monto_total=(precio_producto*cantidad_producto)
# verificador
comprador_compulsivo=(monto_total>300)

#output
print("##############################")
print("# BOLETA DE VENTAS ")
print("#cliente:               ", cliente)
print("#fecha:                 ", fecha)
print("#hora:                  ", hora)
print("#p.u del producto:      ", precio_producto)
print("#cantidad del producto: ",cantidad_producto)
print("#monto total:           ", monto_total)
print("###############################")
# condicional simple
# si el comprador es compulsivo mostrar un descuento en la proxima compra
if(comprador_compulsivo==True):
    print("SE HA GANADO UN DESCUENTO DE 10% EN LA SIGUIENTE COMPRA")
else:
    print("PROCURE COMPRAR MAS LA PROXIMA VEZ")