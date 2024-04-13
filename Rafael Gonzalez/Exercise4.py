def palindromo(palabra):

    palabra = palabra.replace(" ", "").lower()
    
    return palabra == palabra[::-1]

palabra = input ("Escribe tu palabra u oraciÃ³n:")

print(palindromo(palabra))
