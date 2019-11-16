import os
# CALCULO DE LA VELOCIDAD FINAL
velocidad_inicial_1,gravedad_1,ALTURA=0.0,0.0,0.0

# ASIGNACION DE VALORES
velocidad_inicial_1=float(os.sys.argv[1])
gravedad_1=float(os.sys.argv[2])
ALTURA=float(os.sys.argv[3])

# CALCULO
import  math
velocidad_final=math.sqrt((velocidad_inicial_1**2)+2*(gravedad_1*ALTURA))

# CONDICION SIMPLE
if velocidad_final<0:
    print("ERROR,VALORES INCORRECTOS INGRESADOS")

# MOSTRAR VALORES
print("La velocidad inicial del objeto es: "+str(velocidad_inicial_1))
print("La gravedad es: "+str(gravedad_1))
print("La altura es: "+str(ALTURA))
print("La velocidad final del vehiculo es: "+str(velocidad_final))

