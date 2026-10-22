invertir = int(input ("Dime cuanto quieres invertir:"))
interes = float(input("Dime el interes anual:"))
años = int(input ("Dime duarante cuantos años:"))
contador = 1
while contador <= años:
    invertir=(invertir*(1+interes/100))
    print (invertir)
    contador+=1