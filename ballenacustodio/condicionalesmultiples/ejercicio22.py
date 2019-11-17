import os
####hallar el perimetro de un triangulo
####declarar variabes
lado1,lado2,lado3=0.0,0.0,0.0

####input
lado1=float(os.sys.argv[1])
lado2=float(os.sys.argv[2])
lado3=float(os.sys.argv[3])
####processing
perimetro=(lado1+lado2+lado3)

####output
print("##################")
print("#hallar el perimetro de un triangulo")
print("##################")
print("#")
print("##################")
print("#lado1             :",lado1)
print("#lado2             :",lado2)
print("#lado3             :",lado3)
print("#perimetro         :",perimetro)
print("#################")

if(lado1!=lado2 and lado1!=lado3 and lado2!=lado3):
    print("el triangulo es escaleno")
elif(lado1==lado2 and lado1==lado3 and lado2!=lado3):
    print("el triangulo es isosceles")
else:
    print("el triangulo es equilatero")