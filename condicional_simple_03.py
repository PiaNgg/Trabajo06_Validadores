import os
# CALCULO DEL AREA DEL CIRCULO
radio,pi=0.0,0.0

# ASIGNACION DE VALORES
radio=float(os.sys.argv[1])
pi=float(os.sys.argv[2])

# CALCULO
area_del_circulo=str(pi*(radio**2))

# CONDICION SIMPLE
if area_del_circulo<str(0):
    print("ERROR,EL AREA DEL CIRCULO NO PUEDE SER NEGATIVA")
# MOSTRAR VALORES
print("El radio de la circunferencia es: "+str(radio))
print("El valor de pi es: "+str(pi))
print("El area del circulo es: "+area_del_circulo)

