import os
####hallando perimetro del romboide
####declarar variables
base,altura=0.0,0.0

####input
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

####processing
perimetro_romboide=(base+altura)*2

####output
print("###################")
print("#hallar el perimetro del romboide")
print("###################")
print("#")
print("###################")
print("#base              :",base)
print("#altura            :",altura)
print("#perimetro romboide:",perimetro_romboide)
print("###################")
