# Definimos la letra a desplegar
LETTER = "A"
# Solicitamos al usuario el número
number = int(input("\nEscribe un número: "))

# Iteramos para dibujar la piramide
for i in range(1, number * 2):
     if i <= number:
        print(f"{LETTER*i}")
     else:
        print(f"{LETTER*(number*2-i)}")