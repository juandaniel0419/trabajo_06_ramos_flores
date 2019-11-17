import os
# boleta de juegos
#declarar variables
cliente,numero_de_juegos,juegos_ganados,juegos_perdidos,edad,=",",0,0,0,0

#input
cliente=os.sys.argv[1]
numero_de_juegos=int(os.sys.argv[2])
juegos_ganados=int(os.sys.argv[3])
juegos_perdidos=int(os.sys.argv[4])
edad=int(os.sys.argv[5])

##processing
numero_de_victorias=juegos_ganados-juegos_perdidos

#output
print("##########")
print("# BOLETA DE JUEGOS")
print("#######")
print("#cliente  :",cliente)
print("#numero de juegos        :",numero_de_juegos)
print("#juegos ganados          :",juegos_ganados)
print("#juegos perdidos         :",juegos_perdidos)
print("#edad                    :",edad)
print("#numero de victorias     :",numero_de_victorias)
print("#########")
if(edad>18):
    print("puede realizar su juego,es mayor de edad")
if(edad<18):
    print("no puede realizar este juego,no tiene la edad suficiente")
