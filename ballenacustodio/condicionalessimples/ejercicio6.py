import os
####hallar el area del rombo
####declarar variables
diagonal_mayor,diagonal_menor=0.0,0.0

####input
diagonal_mayor=float(os.sys.argv[1])
diagonal_menor=float(os.sys.argv[2])

####processing
area_rombo=(diagonal_mayor*diagonal_menor)/2

####output
print("#####################")
print("#Hallar el area del rombo")
print("#####################")
print("#")
print("#diagonal mayor           :",diagonal_mayor)
print("#diagonal menor           :",diagonal_menor)
print("#area rombo            :",area_rombo)
print("####################")
