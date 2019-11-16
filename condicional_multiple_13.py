# BOLETA DE VENTA DE UN AVION
import os
cliente =  (os.sys.argv[1])
dni =  int(os.sys.argv[2])
hora =  (os.sys.argv[3])
destino =  (os.sys.argv[4])
horas_de_vuelo = int(os.sys.argv[5])
monto_por_hora = int(os.sys.argv[6])
total = horas_de_vuelo * monto_por_hora

print ( " ############################################### ######## " )
print ( " # ´´ALEX PRESS´´´ # " )
print ( " # " )
print ( " # CLIENTE: "  + cliente)
print ( " # DNI: "  +  str (dni))
print ( " # HORARIO DE SALIDA: "  + hora)
print ( " # DESTINO: "  + destino)
print ( " # HORAS DE VUELO: "  +  str (horas_de_vuelo))
print ( " # MONTO POR HORA: "  +  str (monto_por_hora))
print ( " # TOTAL: "  +  str (total))
print ( " # " )
if total >=50:
    print("Vuelo privado")
elif total>=40:
    print("Vuelo clase normal")
elif total>=30:
    print("Vuelo de descuento")
else:
    print("Diviertanse pasajeros")
print ( " ############################################### ######## " )
