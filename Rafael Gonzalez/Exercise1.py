def calcular_cuadrado(numero):
  
    return numero ** 2

while True:
    numero = int(input("Ingresa un número: "))
    if numero <= 100:
        break
    else:
        print("Por favor, ingresa un número igual o menor que 100.")

cuadrado = calcular_cuadrado(numero)
print(f"El cuadrado de {numero} es: {cuadrado}")