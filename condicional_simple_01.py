import os
# CALCULO DEL AREA DE UN TRIANGULO
base,altura=0.0,0.0

# ASIGNACION DE LOS VALORES
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

# CALCULO
area_del_triangulo=(base*altura)/2

# CONDICION SIMPLE
if area_del_triangulo>100:
    print("ES ACTO PARA EL TERRENO")

# MOSTRAR VALORES
print("La base del triangulo es: "+str(base))
print("La altura del triangulo es: "+str(altura))
print("El area del triangulo es: "+str(area_del_triangulo))













































