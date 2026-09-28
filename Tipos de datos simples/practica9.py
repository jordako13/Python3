invertir =  int(input("¿QUe cantidad quieres invertir?: "))
interes = int(input("¿Cual es tu interes actual?: "))
años = int(input("¿Cuantos años quieres invertir?: "))
capital = invertir * (1+interes /100) ** años
print("La capital seria de", capital)