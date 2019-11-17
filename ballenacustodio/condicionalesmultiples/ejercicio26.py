import os
####hallando medida de angulo interno  de un hexagono
####declarar variables
numero_de_lados=0

####input
numero_de_lados=int(os.sys.argv[1])

####processing
medida_de_angulo_interno=(180*(numero_de_lados-2))/numero_de_lados

####output
print("###################")
print("#hallar medida de angulo interno ")
print("###################")
print("#")
print("###################")
print("#numero_de_lados             :",numero_de_lados)
print("#medida del angulo intero:",medida_de_angulo_interno)
print("###################")
if (numero_de_lados==6):
    print("el poligono es un exagono")
else:
    print("el poligono no es un exagono")

