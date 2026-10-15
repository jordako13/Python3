puntuacion = float(input ("Cual es tu puntuación:"))
dinero= 2400*puntuacion
if (puntuacion==0.0):
    print ("Tienes nivel Inaceptable te tienen que dar:", dinero)
elif (puntuacion==0.4):
    print("Tienes nivel Aceptable te tienen que dar:", dinero)
elif (puntuacion>=0.6):
    print("Tienes nivel Meritorio te tienen que dar:", dinero)
    