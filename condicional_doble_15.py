# BOLETA DE VENTA DE UN CONCIERTO
import os
tipo_de_entrada_1 = (os.sys.argv[1])
ripo_De_entrada_2 =  (os.sys.argv[2])
precio_vip =  float(os.sys.argv[3])
precio_general =  float(os.sys.argv[4])
unidades_vip =  int(os.sys.argv[5])
unidades_general =  int(os.sys.argv[6])
TOTAL  = precio_vip * precio_vip + precio_general * unidades_general

print ( " ############################################### ################## " )
print ( " # CONCIERTO ´´ALL STARS´´ # " )
print ( " # # " )
print ( " # ENTRADAS: VIP GENERAL # " )
print ( " # UNIDADES: "  +  "             "  +  str (unidades_vip) +  "                     "  +  str (unidades_general) +  "                      # " )
print ( " # PRECIO: "  +  "               "  +  str (precio_vip) +  "                       "  +  str (precio_general) +  "                        # " )
print ( " # " )
print ( " # " )
print ( " # TOTAL A PAGAR: "  +  str ( TOTAL ))
print ( " # " )
print ( " # " )
if TOTAL>=40500:
    print("Diviertase mucho")
else:
    print("Que tenga buen vuelo")
print ( " ############################################### ################### " )
