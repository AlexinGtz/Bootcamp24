# Definir el límite
LIMIT = 100

while True:
     # Solicitamos al usuario el número
    number = int(input("\nEscribe un número: "))
    
    # Validamos que el número introducido sea mayor a cero y menor o igual al límite
    if number > 0 and number <= LIMIT:
        for i in range(1, number + 1):
            print(f"El cuadrado de: {i} es {i**2}")
        break
