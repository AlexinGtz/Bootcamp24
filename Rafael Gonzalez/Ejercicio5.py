def contar_valor(arreglo, valor):
    contador = 0
    for elemento in arreglo:
        if elemento == valor:
            contador += 1
    return contador

arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]   
     
valor = int(input("ingrese numero del 1 al 9: "))
resultado = contar_valor(arreglo, valor)
print(f"El valor {valor} aparece {resultado} veces en el arreglo.")