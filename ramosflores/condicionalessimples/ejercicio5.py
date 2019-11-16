import os
# boleta de ventas de un taller de mecanica
# declaracion de valores
cliente,fecha,hora,precio_llanta,precio_aros,cantidad_llantas,cantidad_aros="","","",0.0,0.0,0,0

#imput
cliente=os.sys.argv[1]
fecha=os.sys.argv[2]
hora=os.sys.argv[3]
precio_llanta=float(os.sys.argv[4])
precio_aros=float(os.sys.argv[5])
cantidad_llantas=int(os.sys.argv[6])
cantidad_aros=int(os.sys.argv[7])

# prosessing
monto_total=(precio_llanta*cantidad_llantas+precio_aros*cantidad_aros)
# verificador
comprador_compulsivo=(monto_total>2000)

#output
print("##############################")
print("# BOLETA DE VENTAS ")
print("#cliente:             ", cliente)
print("#fecha:               ", fecha)
print("#hora:                ", hora)
print("#p.u por llanta:      ", precio_llanta)
print("#p.u por aros:        ", precio_aros)
print("#cantidad de llantas: ",cantidad_llantas)
print("#cantidad de aros:    ",cantidad_aros)
print("#monto total:       ", monto_total)
print("###############################")
# condicional simple
# si el comprador es compulsivo mostrar un descuento en la proxima compra
if(comprador_compulsivo==True):
    print("SE HA GANADO UN DESCUENTO DE 20% EN SU PROXIMA COMPRA")
# FIN IF
