import os
####comprando audifonos para pc
####declarar variables
cliente,unidades,precio_unitario=",",0,0.0

####input
cliente=os.sys.argv[1]
unidades=int(os.sys.argv[2])
precio_unitario=float(os.sys.argv[3])

####processing
total=precio_unitario*unidades

####output
print("########################")
print("BOLETA DE VENTA")
print("########################")
print("#")
print("#cliente       :",cliente)
print("#unidades        :",unidades)
print("#precio_unitario           :s/.",precio_unitario)
print("#total         :s/.",total)
print("########################")
