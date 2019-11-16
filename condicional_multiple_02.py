import os
# CALCULO DE LA FUERZA DE UN OBJETO
masa,aceleracion=0.0,0.0

# ASIGNACION DE VALORES
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])

# CALCULO
Fuerza=str(masa*aceleracion)

# CONDICION MULTIPLE
if Fuerza>str(20):
    print("FUERZA EXCEDIDA,ROMPERA EL OBJETO")
elif Fuerza==0:
    print("NO HAY FUERZA REALIZADA")
else:
    print("FUERZA ESTABLE, SIGA REALIZANDO EL TRABAJO CON LA ACELERACION CONSTANTE")

# MOSTRAR VALORES
print("La masa del objeto es: "+str(masa))
print("La aceleracion del objeto es: "+str(aceleracion))
print("La fuerza del objeto es: "+Fuerza)

