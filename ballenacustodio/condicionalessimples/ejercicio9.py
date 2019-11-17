import os
####compra de bateria para celular
####declarar datos
cliente,direccion,unidades,precio_unitario=",",",",0,0.0

####input
cliente=os.sys.argv[1]
direccion=os.sys.argv[2]
unidades=int(os.sys.argv[3])
precio_unitario=float(os.sys.argv[4])

####processing
monto_total=(precio_unitario*unidades)

####output
print("################")
print("#BOLETA DE VENTA")
print("################")
print("#")
print("################")
print("#cliente               :",cliente)
print("#direccion             :",direccion)
print("#unidades              :",unidades)
print("#precio unitario       :",precio_unitario)
print("#monto total           .",monto_total)
print("################")
