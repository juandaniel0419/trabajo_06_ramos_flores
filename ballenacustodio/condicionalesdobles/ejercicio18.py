import os
####import os
# boleta de ventas
#declarar variables
cliente,producto,precio,cantidad=",",0.0,0,0
#input
cliente=os.sys.argv[1]
precio=float(os.sys.argv[2])
cantidad=int(os.sys.argv[3])

##processing
monto_total=(precio*cantidad)

#output
print("##########")
print("# BOLETA DE VENTA")
print("#######")
print("#cliente  :",cliente)
print("#precios  :",precio)
print("#cantidad  :",cantidad)
print("#total    :",monto_total)
print("###############")

if (monto_total>500):
    print("Ganaste una prenda")
if(monto_total<500):
    print("sigue intentando ")

