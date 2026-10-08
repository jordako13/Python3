edad = int(input ("Introduce tu edad:"))
ingresos = int(input ("Introduce tus ingresos mensuales:"))
if (edad>16 and ingresos>=1000):
    print ("Tienes que tributar")
else:
    print("No tienes que tributar")