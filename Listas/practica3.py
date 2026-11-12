asignaturas = ["Matematicas","Lengua","Fisica","Quimica","Historia"]
notas = []
for asignatura in asignaturas:
    nota = input(f"Que nota has sacado en la asignatura {asignatura}:")
    notas.append(nota)
for i in range(len(asignaturas)):
    print ("En",asignaturas[i],"has sacado",notas[i])