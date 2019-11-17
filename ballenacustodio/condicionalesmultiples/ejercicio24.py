import os
####ventas de entradas de discoteca
####declarar variables
entradas,costo_entrada,=0,0.0

####input
entradas=int(os.sys.argv[1])
costo_entrada=float(os.sys.argv[2])

####processing
monto_recaudado=(entradas*costo_entrada)

####output
print("###################")
print("#ventas de entradas")
print("#")
print("##################")
print("entradas           :",entradas)
print("#costo entrada     :",costo_entrada)
print("#monto recaudado   :",monto_recaudado)
print("##################")

if(costo_entrada>30):
    print("compraste una entrada vip,que disfrute la noche")
elif(costo_entrada<=30 and costo_entrada>20):
    print("compraste una entrada platinium,que disfrute la noche")
else:
    print("compraste una entrada general,que disfrute la noche")