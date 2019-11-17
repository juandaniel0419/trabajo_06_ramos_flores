import os
#### materiales de construccion
####declarar variables
nombre,materiales,precio_unitario,unidades=",",",",0.0,0

#####input
nombre=os.sys.argv[1]
materiales=os.sys.argv[2]
precio_unitario=float(os.sys.argv[3])
unidades=int(os.sys.argv[4])

####processing
monto=(precio_unitario*unidades)

####0utput
print("###############")
print("# boleta de venta demateriales de construccion")
print("#")
print("###############")
print("#nombre             :",nombre)
print("#materiales         :",materiales)
print("#precio unitario             :",precio_unitario)
print("#unidades           :",unidades)
print("#monto              :",monto)
print("#################")

if (monto>=3000):
    print("gano un descuento del 15% del monto")
elif(monto>=2000 ):
    print("gano una polo")
else:
    print("gracias por su preferencia")