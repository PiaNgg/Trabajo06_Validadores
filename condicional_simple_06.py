import os
# CALCULO DE LA PENDIENTE
abscisa,ordenada=0.0,0.0

# ASIGNACION DE VALORES
abscisa=int(os.sys.argv[1])
ordenada=int(os.sys.argv[2])

# CALCULO
pendiente=ordenada/abscisa

# CONDICIONAL SIMPLE
if abscisa==0:
    print("ERROR VALORES INCORRECTOS INGRESADOS")

# MOSTRAR VALORES
print("El valor de la abscisa es: "+str(abscisa))
print("El valor de la ordenada es: "+str(ordenada))
print("La pendiente tiene valor de: "+str(pendiente))
