

def contar_valores(arreglo, valor): #se define una funcion (contar_valores) con dos parametros: arreglo y valor, donde arreglo guardara los datos ingresados y valor el numero o la palabra la cual se quiere contar dentro del arreglo.
    contador = 0                    #se busca que cada que 'valor' salga dentro de 'arreglo', contador incremente su valor en 1.
    for palabra_o_numero in arreglo:     #el ciclo for ciclara 'palabra o numero' valor por valor dentro del arreglo.
        if palabra_o_numero == valor:
            contador += 1                 #si 'palabra_o_numero' encuentra un elemento igual a 'valor', el contador incrementara 1 y retornara el valor actual a 'contador'.
    return contador

#arreglo = input('Ingresa un arreglo de numero y palabras separados por una coma; \n [Ejemplo: (Rana, 3, Juan, 340, casa)] \n ')
arreglo = []

arreglo_por_usuario = int(input('¿De cuantas palabras será el arreglo?  Ingresa la cantidad total de palabras: \n '))   #el usuario ingresa la cantidad de elementos que desea en el arreglo
for i in range(0, arreglo_por_usuario):    #se hace un bucle para que cada que el usuario ingrese un elemento al arreglo, este se coloque de manera correcta al arreglo.
    print('Agrega el siguiente elemento a la lista ... ')
    arreglo.append(input())
    
elemento_a_contar = input('Que palabra o numero deseas contabilizar dentro del arreglo?:  \n ')

resultado = contar_valores(arreglo, elemento_a_contar) #esta variable manda llamar las veces que el contador fue alterado y lo coteja con la palabra que el usuario haya agregado en 'elemento a contar'

print(f"El valor {elemento_a_contar} aparece {resultado} veces en el arreglo.")

