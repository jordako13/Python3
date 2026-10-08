producto = input("Dime los productos:")
precio = float(input("Dime el precio:"))
cantidad = int(input("Dime la cantidad:"))
total = precio * cantidad
print(f"{producto}: {precio:9.2f}€ X {cantidad:3d} unidades = {total:11.2f}€")