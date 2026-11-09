frase = input("Dime una frase:")
letra = input("Dime una letra para ver cuantas veces aparece:")
contador = 0
for cuenta in frase:
    if cuenta == letra:
        contador += 1
print ("La", letra,"aparece:",contador,"veces")