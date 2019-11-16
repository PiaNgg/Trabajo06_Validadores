import os
# CALCULO DE LA ALTURA DE UN EDIFICIO
velocidad_inicial,tiempo,gravedad=0.0,0.0,0.0

# ASIGANACION DE VALORES
velocidad_inicial=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])
gravedad=float(os.sys.argv[3])

# CALCULO
haltura=velocidad_inicial*tiempo+(gravedad*(tiempo**2))/2

# CONDICION MULTIPLE
if haltura>15:
    print("ES UN EDIFICIO")
elif haltura==0:
    print("PARECE QUE HAY UN ERROR CON LOS VALORES INGRESADOS")
else:
    print("ES UNA CASA")
# MOSTRAR VALORES
print("La velocidad inicial del objeto es: "+str(velocidad_inicial))
print("El tiempo de caida del objeto es: "+str(tiempo))
print("La gravedad con la que cae el objeto es: "+str(gravedad))
print("La altura del edificio es: "+str(haltura))
