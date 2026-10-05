precio = input("Introduce un precio con dos decimales:")
euros = precio.split(",")[0]
centimos = precio.split(",")[1]
print ("En el precio hay", euros, "euros y", centimos, "centimos")