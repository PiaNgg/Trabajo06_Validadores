# BOLETA PRODUCTOS LACTEOS
import os
primer_producto =(os.sys.argv[1])
segundo_producto = (os.sys.argv[2])
P_U_1  =  float (os.sys.argv[3])
P_U_2  =  float (os.sys.argv[4])
unidades_1 =  int (os.sys.argv[5])
unidades_2 =  int (os.sys.argv[6])
total =  P_U_1  * unidades_1 +  P_U_2  * unidades_2

print ( " ############################################### ########### " )
print ( " # BODEGA ´´LA LACTOSA´´ ´ # " )
print ( " # " )
print ( " # PRODUCTOS: "  + primer_producto +  " , "  + segundo_producto)
print ( " # PU 1: "  +  str ( P_U_1 ))
print ( " # PU 2: "  +  str ( P_U_2 ))
print ( " # UNIDADES 1 Y 2: "  +  str (unidades_1) +  " , "  +  str (unidades_2))
print ( " # TOTAL $: "  +  str (total))
print ( " # " )
if total>=50:
    print("No consuma tanto")
elif total>=40and total<50:
    print("Siga asi")
elif total>=30 and total<40:
    print("Debe consumir mas")
else:
    print("Buen trabajo")
print ( " ############################################### ########## " )
