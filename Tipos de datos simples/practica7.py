Peso= float(input("Dime tu peso (en kg): "))
Altura = float(input("Dime tu altura (en metros): "))
IMC = round(Peso/(Altura**2), 2)
print (f"Tu indice de masa corporal es", IMC)