# BOLETA DE VENTA MERCADO SANTA ANITA
import os
carne =(os.sys.argv[1])
P_U  = float(os.sys.argv[2])
unidad_1 = int(os.sys.argv[3])
TOTAL  =  P_U  * unidad_1

print ( " ############################################### # " )
print ( " # MERCADO ´´SANTA ANITA´´ # " )
print ( " # " )
print ( " # TIPO DE CARNE: "  + carne)
print ( " # PU: "  +  str ( P_U ))
print ( " # UNIDADES: "  +  str (unidad_1))
print ( " # TOTAL: "  +  str ( TOTAL ))
print ( " # " )
if TOTAL>=50:
    print("No gaste tanto")
elif TOTAL>=30:
    print("Gasto lo necesario")
elif TOTAL>=20:
    print("Aun tiene dinero")
else:
    print("Continúe así")
print ( " ############################################### # " )
