userQuantity = int(input("Cuantos alumnos hay en el curso?\n"))

studentNames = []
studentAges = []

for i in range(1, userQuantity + 1):
    userName = input(f"Nombre del alumno {i} ")
    userAge = int(input(f"Edad del alumno {i} "))
    studentNames.append(userName)
    studentAges.append(userAge)

print(studentNames)
print(studentAges)

sumOfAges = 0

for counter in range(userQuantity):
    sumOfAges += studentAges[counter]

print(f"El promedio de edad en los alumnos es de: {sumOfAges / userQuantity}")

maxAge = 0
maxAgeIndex = 0

for counter in range(userQuantity):
    if (studentAges[counter] > maxAge):
        maxAge = studentAges[counter]
        maxAgeIndex = counter

print(f"El alumno mas grande es: {studentNames[maxAgeIndex]} con {maxAge} años de edad")

print("inicio del ciclo de nombres")
for nombre in studentNames:
    print(nombre)