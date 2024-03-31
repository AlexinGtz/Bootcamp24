import math
# for x in range(100):
#     print(x)

# x = 60

# while(x < 50):
#     x += 1
#     print(f'Hola a todos {x}')

# userWrongSelection = True
# selectedNumber = 0
# while (userWrongSelection):
#     selectedNumber = int(input('Por favor ingresa un numero\n'))
#     if(selectedNumber < 100 and selectedNumber > 0):
#         userWrongSelection = False
#     else:
#         print('Tu numero es muy grande')

# print(selectedNumber)

# range(5) ---> [0, 1, 2, 3, 4]
for number in range(5):
    print(number)

array = [0, 1, 2, 3, 4]

for data in array:
    print(data)

# for i in range(2,10) --> [2, 3 ,4 ,5 ,6 ,7 ,8 ,9]

estudiantes = ['Juan', 'Manuel', 'Luis', 'Mariana']

for estudiante in estudiantes:
    print(estudiante)

materias = ['Espa;ol', 'Matematicas', 'Ingles', 'Fisica']

for materia in materias:
    print(materia)
print('-=============')
print(materias[1])

cantidadMaterias = len(materias)
print(cantidadMaterias)
print('-=============')
for index in range(cantidadMaterias):
    print(materias[index])

materias[2] = 'Ciencias'

print(materias)
print(materias[0:2])

materias.append('Calculo')

print(materias)

materias.append('Integrales')

print(materias)
materias.pop()
print(materias)

materias.append(['Aerodinamica', 'Fluidos'])

print(materias)
materias.pop()

materias.extend(['Aerodinamica', 'Fluidos'])

print(materias)

test = materias + [1, 2]

print(test)
print(materias)

print([1, 2] * 4)

databaseNumbers = [1,2,3,4,5,62,4563,782,345,1274,643]

even = []
odds = []

for number in databaseNumbers:
    print(number)
    if(number % 2 == 0):
        even.append(number)
    else:
        odds.append(number)

print('Pares: ', even)
print('Nones: ', odds)

# suma
a = 2 + 2
print(a)
# resta
b = 2 - 2
print(b)
# multiplicacion
c = 2 * 2
print(c)
# division
d = 2 / 2
print(d)
# division flotante
e = 3 / 2
print(e)
# division entera
f = 2 // 2
print(f)
# division entera 
g = 3 // 2
print(g)
# remanente
h = 2 % 2
print(h) 
# remanente
i = 3 % 2
print(i) 
# division entera con MATH
j = math.floor(3 / 2)
print(j)
# potencias
k = 2 ** 4
print(k)
# potencias con MATH
l = math.pow(2, 4)
print(l)
# raiz
m = math.sqrt(4)
print(m)

print(math.sin(12))