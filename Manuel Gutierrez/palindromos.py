def esPalindromo (palabra: str):
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    palabra = palabra.replace("á", "a")
    palabra = palabra.replace("é", "e")
    palabra = palabra.replace("í", "i")
    palabra = palabra.replace("ó", "o")
    palabra = palabra.replace("ú", "u")

    inicio_palabra = 0
    fin_palabra = len(palabra) - 1
   
    for letra in range(0 , len(palabra)):
        if palabra [inicio_palabra] == palabra [fin_palabra]:
            inicio_palabra += 1
            fin_palabra -= 1
        else:
            return False
    return True

palabra = input('Ingrese una palabra: \n')

if esPalindromo(palabra):
    print(f'La letra o frase {palabra} sí es palíndromo.')
else:
    print(f'La palabra o frase {palabra} no es palíndromo.')