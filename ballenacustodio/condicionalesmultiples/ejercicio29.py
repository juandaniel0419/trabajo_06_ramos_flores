import os
####suma de angulos internos de un cuadrilatero
####declarar variables
angulo1,angulo2,angulo3,angulo4=0.0,0.0,0.0,0.0

####input
angulo1=float(os.sys.argv[1])
angulo2=float(os.sys.argv[2])
angulo3=float(os.sys.argv[3])
angulo4=float(os.sys.argv[4])

####processing
suma_de_angulos_internos_cuadrilatero=(angulo1+angulo2+angulo3+angulo4)


####output
print("###################")
print("#suma de angulos internos de un cuadrilatero ")
print("###################")
print("#")
print("###################")
print("#angulo1                                :",angulo1)
print("angulo2:                                :",angulo2)
print("#angulo3                                :",angulo3)
print("#angulo4                                :",angulo4)
print("#suma de angulos internos cuadrilatero  :",suma_de_angulos_internos_cuadrilatero)
print("###################")
if (suma_de_angulos_internos_cuadrilatero>360):
    print("el cuadrilatero no existe")
elif(suma_de_angulos_internos_cuadrilatero==360):
    print("es un cuadrilatero")
else:
    print("no existe")

