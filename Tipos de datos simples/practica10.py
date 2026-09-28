peso_payaso = 112
peso_muñeca = 75
payasos_vendidos = int(input("Cuantos payasos hemos vendido?: "))
muñecas_vendidas = int(input("Cuantas muñecas hemos vendido?: "))
peso_total = (peso_payaso * payasos_vendidos) + (peso_muñeca * muñecas_vendidas)
print ("El paquete pesa", peso_total, "se vendieron", payasos_vendidos, "payasos y", muñecas_vendidas, "muñecas")