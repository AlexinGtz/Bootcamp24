
#CALCULADORA usando FUNCIONES



def calculator (operation, valor1=int, valor2=int):
    if operation == 1:
        addition = valor1 + valor2
        return addition
    elif operation == 2:
        subtraction = valor1 - valor2
        return subtraction
    elif operation == 3:
        division = valor1 / valor2
        return division
    elif operation == 4:
        multiplication = valor1 * valor2
        return multiplication
    
operation = int(input('\n Choose one operation:   \n \nAddition - Press "1"\nSubtraction - Press "2"\nDivision - Press "3"\nMultiplication - Press "4" \n '))    
valor1 = int(input('Enter first number:     '))
valor2 = int(input('Enter second number:    '))        

results= calculator(operation, valor1, valor2)

print(f'\n Your result is {results}')