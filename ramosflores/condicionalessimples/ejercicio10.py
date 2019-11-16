import os
# boleta de ventas de un supermercado
# declaracion de variables
cliente,vendedor,hora,fecha,p1,p2,p3,p4,cantidad_p1,cantidad_p2,cantidad_p3,cantidad_p4,pr1,pr2,pr3,pr4="","","","","","","","",0,0,0,0,0.0,0.0,0.0,0.0

#imput
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
hora=os.sys.argv[3]
fecha=os.sys.argv[4]
p1=os.sys.argv[5]
p2=os.sys.argv[6]
p3=os.sys.argv[7]
p4=os.sys.argv[8]
cantidad_p1=int(os.sys.argv[9])
cantidad_p2=int(os.sys.argv[10])
cantidad_p3=int(os.sys.argv[11])
cantidad_p4=int(os.sys.argv[12])
pr1=float(os.sys.argv[13])
pr2=float(os.sys.argv[14])
pr3=float(os.sys.argv[15])
pr4=float(os.sys.argv[16])

# prosessing
total=(cantidad_p1*pr1)+(cantidad_p2*pr2)+(cantidad_p3+pr3)+(cantidad_p4+pr4)
# verificador
comprador_complusivo=(total>300)

#output
print("#################################################")
print("BOLETA DE VENTAS")
print("cliente        :                      ", cliente)
print("vendedor       :                      ", vendedor)
print("hora           :                      ", hora)
print("fecha          :                      ", fecha)
print("producto 1     :                      ", p1)
print("producto 2     :                      ", p2)
print("producto 3     :                      ", p3)
print("prodcuto 4     :                      ", p4)
print("cantidad 1     :                      ", cantidad_p1)
print("cantidad 2     :                      ", cantidad_p2)
print("cantidad 3     :                      ", cantidad_p3)
print("cantidad 4     :                      ", cantidad_p4)
print("precio 1       :                      ", pr1)
print("precio 2       :                      ", pr2)
print("precio 3       :                      ", pr3)
print("precio 4       :                      ", pr4)
print("monto total    :                      ", total)
print("####################################################")

if(comprador_complusivo==True):
    print("SE HA GANADO BONO POR HABER SUPERADO 300 DE COMPRA")

# IF FIN

