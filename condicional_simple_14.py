# BOLETA DE VENTA DE UNA PANADERIA
import os
tipo_pan_1 =(os.sys.argv[1])
tipo_de_pan_2 = (os.sys.argv[2])
P_U_1  = float(os.sys.argv[3])
P_U_2  = float(os.sys.argv[4])
unidades_1 =  int (os.sys.argv[5])
unidades_2 =  int (os.sys.argv[6])
TOTAL  =  P_U_1  * unidades_1 +  P_U_2  * unidades_2

print ( " ############################################### ######## " )
print ( " # PANADERIA ´´DON JUAN´´ # " )
print ( " # " )
print ( " # PRIMER TIPO DE PAN: "  + tipo_pan_1)
print ( " # SEGUNDI TIPO DE PAN: "  + tipo_de_pan_2)
print ( " # PU 1: "  +  str ( P_U_1 ))
print ( " # PU 2: "  +  str ( P_U_2 ))
print ( " # UNIDADES 1 °: "  +  str (unidades_1))
print ( " # UNIDADES 2 °: "  +  str (unidades_2))
print ( " # TOTAL A PAGAR: "  +  str ( TOTAL ))
print ( " # " )
if TOTAL>=12:
    print("No coma mucha caloria")
print ( " ############################################### ########## " )

