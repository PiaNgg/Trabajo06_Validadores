# BOLETA DE VENTA DE UNA TIENDA TECNOLOGIDCA
import os
producto_1 =(os.sys.argv[1])
P_U  =  float(os.sys.argv[2])
unidades =  int(os.sys.argv[3])
NOMBRE  = (os.sys.argv[4])
TOTAL  =  P_U  * unidades
IGV  =  TOTAL  *  0.18

print ( " ############################################### ############ " )
print ( " # TIENDA ´´ELECKTROMAC´´ # " )
print ( " # " )
print ( " # CLIENTE: "  +  NOMBRE )
print ( " # PRODUCTO: "  + producto_1)
print ( " # PU: "  +  str ( P_U ))
print ( " # UNIDADES: "  +  str (unidades))
print ( " # IGV: "  +  str ( IGV ))
print ( " # TOTAL: "  +  str ( TOTAL ))
print ( " # " )
if TOTAL>=10000:
    print("Usted es un consumidor gold")
elif TOTAL>=80000:
    print(("Usted es cluente platino"))
elif TOTAL>=60000:
    print("Usted está cerca a ser un cliente reconocido")
else:
    print("Continue hasta llegar a ser un buen cliente")
print ( " ############################################### ############ " )
