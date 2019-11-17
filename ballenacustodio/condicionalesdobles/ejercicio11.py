import os
####horas semanales trabajadas de un empleado,si las horas trabajadas superan los 40,recibe bonificacion de 100
####declarar datos
nombre_empleado,numero_de_horas,pago_por_hora=",",0,0.0

####input
nombre_empleado=os.sys.argv[1]
numero_de_horas=int(os.sys.argv[2])
pago_por_hora=float(os.sys.argv[3])

####processing
sueldo=(numero_de_horas*pago_por_hora)+100

####verificador
buen_empleado=(numero_de_horas>40)


####output
print("############")
print("BOLETA DE SALARIO")
print("############")
print("#")
print("############")
print("#nombre del empleado          :",nombre_empleado)
print("#numero de horas              :",numero_de_horas)
print("#pago por hora                :",pago_por_hora)
print("#sueldo                       .",sueldo)
print("############")

####condicional doble
#si trabajador es buen empleado ,mostrarle la bonificacion
if(buen_empleado == true):
    print("ganaste la bonificacion")

