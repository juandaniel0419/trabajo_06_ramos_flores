import os
# boleta de ventas
# declaracion de variables
cliente,producto,precio,cantidad="","",0.0,0
# imput
cliente=os.sys.argv[1]
producto=os.sys.argv[2]
precio=float(os.sys.argv[3])
cantidad=int(os.sys.argv[4])


# PROCESSING
monto_total=round(precio*cantidad)

# VERIFICADOR
comprador_compulsivo=(cantidad>10)

# OUTPUT
print("########################")
print("# BOLETA DE VENTAS")
print("#cliente", cliente)
print("#producto", producto)
print ("# Cantidad:", cantidad)
print ("# Monto total:", monto_total)

# Condicion Simple
# si el comprador es compulsivo, mostrarle la tarjeta dorada
if (comprador_compulsivo==True):
    print ("GANASTE UNA ENTRADA PARA EL CINE")

if(comprador_compulsivo<5):
    print("vuelva pronto,gracias por su compra")

if(comprador_compulsivo<10):
    print("estuvo a punto de ganar una entrada al cine,procure comprar mas")