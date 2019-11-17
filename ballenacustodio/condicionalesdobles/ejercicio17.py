import os
####sueldo de un trabajador despues de gastos personales
####declarar variables
ingresos_mensuales,egresos_mensuales,=0.0,0.0
####input
ingresos_mensuales=float(os.sys.argv[1])
egresos_mensuales=float(os.sys.argv[2])

####processing
monto_restante=(ingresos_mensuales-egresos_mensuales)

####output
print("#############")
print("ingresos_mensuales")
print("################")
print("#ingresos_mensuales       :",ingresos_mensuales)
print("#egresos_mensuales        :",egresos_mensuales)
print("monto_restante            :",monto_restante)
print("###############")

if(ingresos_mensuales>egresos_mensuales):
    print("ahorrador")
if(ingresos_mensuales<egresos_mensuales):
    print("endeudado")