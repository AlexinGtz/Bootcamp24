seleccion = int(input("Elige la operación, 0.-Suma, 1.-Resta, 2.-Multiplicación, 3.-División: "))
i = 10

if seleccion == 0:
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    res= n1 + n2
    print ("El resultado de su suma es:", res)
    print ("Gracias")
if seleccion == 1:
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    res= n1 - n2
    print ("El resultado de su resta es:", res)
    print ("Gracias")
if seleccion == 2:
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    res= n1 * n2
    print ("El resultado de su multiplicación es:", res)
    print ("Gracias")
if seleccion == 3:
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))
    res= n1 / n2
    print ("El resultado de su división es:", res)
    print ("Gracias")

if seleccion != i:
    print ("Ingrese un valor valido")
 