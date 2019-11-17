import os
####promedio de 6 notas de programacion
###declarar variables
nota1,nota2,mota3,nota4,nota5,nota6=0,0,0,0,0,0
####input
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
nota4=int(os.sys.argv[4])
nota5=int(os.sys.argv[5])
nota6=int(os.sys.argv[6])

####processing
promedio=(nota1+nota2+nota3+nota4+nota5+nota6)/6

####output
print("##########")
print("#promedio de notas")
print("########")
print("#nota1   :",nota1)
print("#nota2   :",nota2)
print("#nota3   :",nota3)
print("#nota4   :",nota4)
print("#nota5   :",nota5)
print("#nota6   :",nota6)
print("#promedio:",promedio)
print("########")
