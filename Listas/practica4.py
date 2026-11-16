numeros_ganadores =[]
for i in range(6):
    numero = int(input("Introduce un numero ganador:"))
    numeros_ganadores.append(numero)
    numeros_ganadores.sort()
    print ("Los numeros ganadores de menor a mayor son:", numeros_ganadores)