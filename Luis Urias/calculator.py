# python 3.11 para uso del match-case

# Definimos las opciones disponibles
OPTIONS = 4

title = "\nCALCULADORA\n\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n\n"

while True:
    # Solicitamos la operación
    operation = int(input(f"{title}Selecciona una operación: "))
    
    # Revisamos que la operación sea valida
    if operation > 0 and operation <= OPTIONS:
        number_one = int(input("\nIntroduce el primer número entero: "))
        number_two = int(input("\nIntroduce el segundo número entero: "))
        match operation:
            case 1: 
                print(f"\nEl resultado es: {number_one + number_two}\n")
            case 2:
                print(f"\nEl resultado es: {number_one - number_two}\n")
            case 3:
                print(f"\nEl resultado es: {number_one * number_two}\n")
            case 4:
                print(f"\nEl resultado es: {round(number_one / number_two,2)}\n")

        break
           