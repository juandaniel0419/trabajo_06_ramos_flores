import os
####hallar el volumen de una prisma
####declarar variables
area_de_la_base,altura=0.0,0.0

####input
area_de_la_base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])
####processing
volumen=(area_de_la_base*altura)


####output
print("###################")
print("#hallar volumen de la prisma ")
print("###################")
print("#")
print("###################")
print("#area de la base           :",area_de_la_base)
print("#altura         :",altura)
print("#volumen        :",volumen)
print("###################")
if (area_de_la_base==altura):
    print("el prisma es regular")
elif(area_de_la_base>altura):
    print("el prisma es oblicuo")
else:
    print("el prisma es irregular")

