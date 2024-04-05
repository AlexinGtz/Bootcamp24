import math

# def calculateForce(mass, acceleration):
#     force = mass * acceleration
#     return force

# def isUserAnAdmin(token):
#     if(token == 'admin'):
#         return True
#     else:
#         return False
# #--------------------------------------
# carForce = calculateForce(2000, 15)
# boyForce = calculateForce(50, 2)

# print(carForce)
# print(boyForce)

# angle = math.sin(0.50)
# print(angle)

# isAdmin = isUserAnAdmin('admin')

# if(isAdmin):
#     print('El usuario es admin')
# else:
#     print('Saquese usuario normal')

def Fibonacci(number):
    if(number == 0):
        return
    secondLastNumber = 0
    lastNumber = 1
    print(secondLastNumber)
    print(lastNumber)
    for i in range(number - 2):
        newNumber = lastNumber + secondLastNumber
        secondLastNumber = lastNumber
        lastNumber = newNumber
        print(newNumber)

# while True:
#     userInput = int(input('Dame un numero \n'))

#     Fibonacci(userInput)

# def Factorial(number):
#     res = 1
#     for i in rnge(1, number + 1):
#         res *= i

#     return res

# def RecursiveFactorial(number):
#     if(number == 1):
#         return 1
#     return number * RecursiveFactorial(number - 1)

# while True:
#     userInput = int(input('Que factorial quieres \n'))

#     fact = Factorial(userInput)
#     recFact = RecursiveFactorial(userInput)
#     print(fact)
#     print(recFact)

ciclos = 5

for i in range(1, ciclos):
    print(i)

user = 'maestro'

tareas = 0

if(user == 'maestro'):
    print('Eres maestro')
    tareas = 0
elif(user == 'alumno'):
    print('Eres alumno')
    tareas = 5

print(f'Tu numero de tareas es {tareas}')

def func(param1, param2, param3):
    pass

func(param2='valor', param1='otro valor', param3='asdba')