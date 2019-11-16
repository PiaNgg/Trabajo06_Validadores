import os
# CALCULO DEL TRABAJO REALIZADO DE UN OBJETO
fuerza,distancia=0.0,0.0

# ASIGNACION DE  LOS VALORES
fuerza=int(os.sys.argv[1])
distancia=int(os.sys.argv[2])

# CALCULO
trabajo=distancia*fuerza

# CONDICION MULTIPLE
if trabajo<0:
     print("EL TRABAJO REALIZADO ES HACIA LA IZQUIERDA")
elif trabajo==0:
     print("NO HAY TRABAJO REALIZADO")
else:
     print("EL TRABAJO REALIZADO ES HACIA LA DERECHA")
# MOSTRAR VALORES
print("La fuerza del objeto es: "+str(fuerza))
print("La distancia recorrida por el objeto es: "+str(fuerza))
print("El trabajo realizado por un objeto es: "+str(trabajo))
