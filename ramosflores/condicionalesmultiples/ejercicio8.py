import os
# boleta de ventas
# declaracion de valores
cliente,fecha,hora,producto,precio_producto,cantidad_producto="","","","",0.0,0

#imput
cliente=os.sys.argv[1]
fecha=os.sys.argv[2]
hora=os.sys.argv[3]
producto=os.sys.argv[4]
precio_producto=float(os.sys.argv[5])
cantidad_producto=int(os.sys.argv[6])


# prosessing
monto_total=(precio_producto*cantidad_producto)
# verificador
comprador_compulsivo=(monto_total>500)

#output
print("##############################")
print("# BOLETA DE VENTAS ")
print("#cliente:               ", cliente)
print("#fecha:                 ", fecha)
print("#hora:                  ", hora)
print("#producto:              ", producto)
print("#p.u del producto:      ", precio_producto)
print("#cantidad del producto: ",cantidad_producto)
print("#monto total:           ", monto_total)
print("###############################")
# condicional simple
# si el comprador es compulsivo mostrar que esta en un sorteo para un viaje
if(comprador_compulsivo==True):
    print("ESTA PARTICIPANDO DE UN SORTEO PARA UN VIAJE TODO PAGADO ")
if(comprador_compulsivo<200):
    print("ES UN COMPRADOR ORDINARIO,VUELVA PRONTO")
if(comprador_compulsivo<400):
    print("ESTA CASI DE LOGRARLO, VUELVA PRONTO Y COMPRE MAS")