operation = str(input("Pon la operación que deseas hacer '+ , - , * , /:   "))
print(f"Has elegido {operation}")

number = int(input("Pon el primer numero que deseas usar:   "))
number2 = int(input("Pon el segundo numero que deseas usar:   "))

if operation == '+':
    result = number + number2
    print(result)
elif operation == '-':
    result = number - number2
    print(result)
elif operation == '*':
    result = number * number2
    print(result)
elif operation == '/':
    result = number / number2
    print(result)
else:
    print(operation + 'no es un operador válido.')