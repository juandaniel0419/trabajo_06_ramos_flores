import os
####hallar area del triangulo
####declarar variabes
base,altura=0.0,0.0

####input
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

####processing
area_triangulo=(base*altura)/2

####output
print("##################")
print("#hallar el area de un triangulo")
print("##################")
print("#")
print("##################")
print("#base             :",base)
print("#altura           :",altura)
print("#area triangulo   :",area_triangulo)
print("#################")

if(base==altura):
    print("el triangulo es isosceles")
if (base>altura):
    print("el triangulo es escaleno")