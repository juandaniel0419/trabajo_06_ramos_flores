import os
####trabajos de analisis
####declarar variables
ejercicios_propuestos,ejercicios_resueltos,ejercicios_no_resueltos=0,0,0
####input
ejercicios_propuestos=int(os.sys.argv[1])
ejercicios_resueltos=int(os.sys.argv[2])
ejercicios_no_resueltos=int(os.sys.argv[3])

####processing
nota=(ejercicios_resueltos/ejercicios_propuestos)*100
ejercicios_no_resueltos=(ejercicios_propuestos-ejercicios_resueltos)
####output
print("##########")
print("trabajo de analisis")
print("#########")
print("#ejercicos_propuestos      :",ejercicios_propuestos)
print("#ejercicios_resueltos      :",ejercicios_resueltos)
print("#ejercicios no resueltos   :",ejercicios_no_resueltos)
print("#nota                      :",nota)
print("###########")

if(ejercicios_resueltos>ejercicios_no_resueltos):
    print("buen alumno")
if(ejercicios_resueltos<ejercicios_no_resueltos):
    print("mal alumno")