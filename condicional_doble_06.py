import os
# CALCULO DE LA PENDIENTE
abscisa,ordenada=0.0,0.0

# ASIGNACION DE VALORES
abscisa=int(os.sys.argv[1])
ordenada=int(os.sys.argv[2])

# CALCULO
pendiente=ordenada/abscisa

# CONDICIONAL DOBLE
if abscisa==0:
    print("ERROR VALORES INCORRECTOS INGRESADOS")
else:
    print("EL VALOR DE LA ABCISA ES CORRECTO")
# MOSTRAR VALORES
print("El valor de la abscisa es: "+str(abscisa))
print("El valor de la ordenada es: "+str(ordenada))
print("La pendiente tiene valor de: "+str(pendiente))
