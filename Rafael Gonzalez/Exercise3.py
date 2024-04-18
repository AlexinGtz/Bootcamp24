def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    else:
        return num1 / num2

print("Bienvenido a la calculadora simple.")

# Solicitar al usuario que elija la operación
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Por favor, elija una operación (1/2/3/4): ")

# Solicitar al usuario los números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Realizar la operación seleccionada
if opcion == '1':
    resultado = suma(num1, num2)
elif opcion == '2':
    resultado = resta(num1, num2)
elif opcion == '3':
    resultado = multiplicacion(num1, num2)
elif opcion == '4':
    resultado = division(num1, num2)
else:
    print("Opción no válida.")
    resultado = None

# Imprimir el resultado
if resultado is not None:
    print("El resultado de la operación es:", resultado)