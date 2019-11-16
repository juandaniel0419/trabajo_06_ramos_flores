import os
# boleta de notas de colegio
# declaracion de variables
alumno,matematica,lenguaje,biologia,fisica="",0.0,0.0,0.0,0.0

# imput
alumno=os.sys.argv[1]
matematica=float(os.sys.argv[2])
lenguaje=float(os.sys.argv[3])
biologia=float(os.sys.argv[4])
fisica=float(os.sys.argv[5])

# prosessing
nota_final=(matematica+lenguaje+biologia+fisica)/4
# verificador
alumno_repitente=(nota_final<10.5)

# output
print("###############################3")
print("# BOLETA DE NOTAS")
print("#alumno:                ", alumno)
print("#nota de matematica:    ", matematica)
print("#nota de lenguaje:      ", lenguaje)
print("#nota de fisica:        ", fisica)
print("#nota final:            ", nota_final)
print("##################################")

#condicioanl
# si el alumno sale con menos de 10 puntos se mostrara lo siguiente
if(alumno_repitente==True):
    print("EL ALUMNO PODORIA REPETIR EL AÑO")

# FIN IF