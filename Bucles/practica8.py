numero = int(input("Introduce un número entero: "))
for contador in range(1, numero + 1, 2):
    for impares in range(contador, 0, -2):
        print(impares, end=" ")
    print()