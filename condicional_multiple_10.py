import os
# CALCULO DE LA EFICIENCIA DE UNA MAQUINA
energia_total,energia_perdida,energia_util=0.0,0.0,0.0

# ASIGNACION DE VALORES
energia_total=int(os.sys.argv[1])
energia_perdida=int(os.sys.argv[2])

# CALCULO
energia_util=energia_total-energia_perdida
eficiencia_de_una_maquina=(energia_util/energia_total)*100

# CONDICION MULTIPLE
if energia_total==0:
    print("NO HAY ENERGIA TRABAJANDO")
elif energia_total==energia_perdida:
    print("ERROR LOS VALORES INGRESADOS SON INCORRECTOS")
else:
    print("LA ENERGIA SUMINISTRADA ES CORRECTA")
# MOSTRAR VALORES
print("La energia total de una maquina es: "+str(energia_total))
print("La energia perdida de una maquina es: "+str(energia_perdida))
print("La energia util de una maquina es: "+str(energia_util))
print("La eficiencia de una maquina es: "+str(eficiencia_de_una_maquina))
