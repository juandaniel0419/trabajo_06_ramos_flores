import os
# boleta de ventas
#declarar variables
cliente,producto,precio,cantidad,edad=",",0.0,0,0,0
#input
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])
edad=int(os.sys.argv[5])

##processing
monto_total=(precio*cantidad)

#output
print("##########")
print("# BOLETA DE VENTA")
print("#######")
print("#cliente  :",cliente)
print("#producto :",producto)
print("#precios  :",precio)
print("#cantidad  :",cantidad)
print("#edad     :",edad)
print("#monto total    :",monto_total)
print("#########")

if (edad>60):
    print("ganaste un descuento del 15%")

if(edad<60):
    print("ganaste un descuento del 5%")

