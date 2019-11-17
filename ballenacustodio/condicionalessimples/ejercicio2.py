import os
####trabajos de analisis
####declarar variables
ejercicios_propuestos,ejercicios_resueltos=0,0
####input
ejercicios_propuestos=int(os.sys.argv[1])
ejercicios_resueltos=int(os.sys.argv[2])

####processing
nota=(ejercicios_resueltos/ejercicios_propuestos)*100

####output
print("##########")
print("trabajo de analisis")
print("#########")
print("#ejercicos_propuestos      :",ejercicios_propuestos)
print("#ejercicios_resueltos      :",ejercicios_resueltos)
print("#nota                      :",nota)
print("###########")


