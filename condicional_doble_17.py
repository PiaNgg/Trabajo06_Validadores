# BOLETA DE VENTA DE UTILES DE ASEO PERSONAL
import os
producto_1 = (os.sys.argv[1])
precio_del_producto =  float(os.sys.argv[2])
unidades =  int (os.sys.argv[3])
total = precio_del_producto * unidades

print ( " ############################################### ########## " )
print ( " # ´´SIEMPRE SALUD´´ # " )
print ( " # " )
print ( " # PRODUCTO: "  + producto_1)
print ( " # PU: "  +  str (precio_del_producto))
print ( " # UNIDADES: "  +  str (unidades))
print ( " # TOTAL: "  +  str (total))
print ( " # " )
if total>=20:
    print("Ganó un vale de descuento del 10%")
else:
    print("En compras como esta podria ganar descuentos")
print ( " ############################################### ########## " )
