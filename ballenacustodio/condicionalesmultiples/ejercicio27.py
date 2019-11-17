import os
####hallar el volumen de una esfera
####declarar variables
pi,radio=0.0,0.0

####input
pi=float(os.sys.argv[1])
radio=float(os.sys.argv[2])
####processing
volumen=(4/3*(pi*radio**3))
####output
print("###################")
print("#hallar volumen de la esfera ")
print("###################")
print("#")
print("###################")
print("#pi             :",pi)
print("#radio          :",radio)
print("#volumen        :",volumen)
print("###################")
if (volumen>=200):
    print("la esfera es grande")
elif(volumen<=50):
    print("la esfera es mediana")
else:
    print("la esfera es pequeña")

