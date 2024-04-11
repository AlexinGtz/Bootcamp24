def palindromo(palabra):

    palabra = palabra.replace(" ", "").lower()
    
    return palabra == palabra[::-1]

palabra = input ("Escribe tu palabra u oración:")

print(palindromo(palabra))
