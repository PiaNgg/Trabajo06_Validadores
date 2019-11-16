# BOLETA DE VENTA DE BEBIDA ASLCOLICAS
import os
bebida =  (os.sys.argv[1])
precio =  float(os.sys.argv[2])
unidades =  int(os.sys.argv[3])
total = precio * unidades
igv = total *  0.18

print ( " ############################################## " )
print ( " # LICOLERIA EL PARAISO # " )
print ( " # " )
print ( " # PRODUCTO: "  + bebida)
print ( " # PU: "  +  str (precio))
print ( " # UNIDADES: "  +  str (unidades))
print ( " # IGV: "  +  str (igv))
print ( " # TOTAL A PAGAR: "  +  str (total))
print ( " # " )
if total>=160:
    print("Tomar bebidas alcoholicas en exceso es dañino")
elif total>=140:
    print("Si toma no maneje")
elif total>=100:
    print("si sufre de alguna enfermedad tenga cuidado")
else:
    print("No exceda la cantidad")
print ( " ############################################### " )
