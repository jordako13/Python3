contraseña = "condicionales"
contraseña_usuario = str(input ("Introduce la contraseña: "))
contraseña_min = contraseña_usuario.lower()
if (contraseña_min == contraseña):
    print("Esa es la contraseña")
else:
    print("No es la contraseña")