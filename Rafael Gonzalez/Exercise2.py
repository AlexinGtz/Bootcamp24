def imprimir_piramide(numero):
  
    for i in range(1, numero + 1):
        print("A" * i)

    for i in range(1, numero + 1):
        esp = numero-i
        print("A"*esp)    
try:
    numero = int(input("Ingresa un número para la altura de la pirámide: "))
    imprimir_piramide(numero)
except ValueError:
    print("Por favor, ingresa un número válido.")
