import os
####hallar el area de una elipse
####declarar datos
eje_mayor,eje_menor=0.0,0.0

####input
eje_mayor=float(os.sys.argv[1])
eje_menor=float(os.sys.argv[2])

####processing
area_elipse=(eje_mayor*eje_menor)/2
# VERIFICADOR
positiva=(area_elipse>3)

####output
print("###################")
print("#Hallar el area de una elipse")
print("###################")
print("#")
print("###################")
print("#eje mayor               :",eje_mayor)
print("#eje menor               :",eje_menor)
print("#area elipse             :",area_elipse)
print("###################")
if(area_elipse==True):
    print("EL AREA DE LA ELIPSE ES CORRECTA")
