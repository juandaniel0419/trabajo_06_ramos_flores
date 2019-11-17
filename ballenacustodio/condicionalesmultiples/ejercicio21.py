import os
####promedio de 4 notas del alumno del curso "diseño"
####declarar variables
nota1,nota2,nota3,nota4,nombre_del_alumno,=0,0,0,0,",",


####input
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
nota4=int(os.sys.argv[4])
nombre_del_alumno=os.sys.argv[5]

####processing
promedio=(nota1+nota2+nota3+nota4)/4

####output
print("####################")
print("#PROMEDIO DE NOTAS")
print("####################")
print("#")
print("####################")
print("#nota1             :",nota1)
print("#nota2             :",nota2)
print("#nota3             :",nota3)
print("#nota4             :",nota4)
print("nombre del alumno  .",nombre_del_alumno)
print("#promedio          .",promedio)
print("####################")


if(promedio>=17):
    print("muy bueno")
elif(promedio>=14 and promedio<=17):
    print("bueno")
elif(promedio>10 and promedio<=14):
    print("regular")
else:
    print("malo")

