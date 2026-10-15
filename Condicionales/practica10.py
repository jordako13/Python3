tipo = input ("¿Quieres una pizza vegetariana o no vegetariana:")
if (tipo == "vegetariana"):
    print ("Ingredientes: Pimiento y tofu")
    ingrediente= input("Cual quieres elegir?:")
    print ("Tu pizza seria vegetariana y tendria Mozzarella, tomate y", ingrediente)
elif (tipo == "no vegetariana"):
    print ("Ingredientes: Peperoni, Jamon y Salmon")
    ingrediente= input("Cual quieres elegir?:")
    print ("Tu pizza seria no vegetariana y tendria Mozzarella, tomate y", ingrediente)
else:
    print ("Eso no es una pizza")