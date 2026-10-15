renta = int(input ("Cual es tu renta:"))
if (renta < 10000):
    print ("Tu tipo de impositivo es del 5%")
elif (renta < 20000):
    print ("Tu tipo de impositivo es del 15%")
elif (renta < 35000):
    print ("Tu tipo de impositivo es del 20%")
elif (renta < 60000):
    print ("Tu tipo de impositivo es del 30%")
else:
    print ("Tu tipo de impositivo es del 45%")