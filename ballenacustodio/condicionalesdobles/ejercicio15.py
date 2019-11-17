import os
####hallar el area de un rectangulo
####declarar variables
base,altura=0.0,0.0

####input
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

####processing
area_rectangulo=(base*altura)

####output
print("####################")
print("#HALLAR AREA DEL RECTANGULO")
print("#")
print("####################")
print("#base               :",base)
print("#altura             :",altura)
print("#area rectangulo    :",area_rectangulo)
print("###################")

if (base==altura):
    print("es un cuadrado")
if(base>altura or base<altura):
    print("es un rectangulo")
