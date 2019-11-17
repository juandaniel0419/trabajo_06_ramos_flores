import os
####boleta de pago de un banco
####declarar variables
nombre,direccion,monto_cobranza,pago_del_deudor,fecha_de_pago=",",",",0.0,0.0,0

####input
nombre=os.sys.argv[1]
direccion=os.sys.argv[2]
monto_cobranza=float(os.sys.argv[3])
pago_del_deudor=float(os.sys.argv[4])
fecha_de_pago=int(os.sys.argv[5])

####processing
vuelto=(pago_del_deudor-monto_cobranza)

####output
print("###################")
print("#BOLETA DE PAGO")
print("#")
print("###################")
print("#nombre            :",nombre)
print("#direccion         :",direccion)
print("#monto de cobranza :",monto_cobranza)
print("#pago del deudor   :",pago_del_deudor)
print("#fecha de pago     :",fecha_de_pago)
print("#vuelto            :",vuelto)
print("###################")

if(fecha_de_pago<=18 and fecha_de_pago>17 ):
    print("puede pagar su deuda,hoy es ultimo dia")
elif(fecha_de_pago<=15):
    print("puede pagar su deuda,gracias por su putualidad")
else:
    print("se le agregara un recargo,cliente moroso")
