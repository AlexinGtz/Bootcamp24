#Hacer una función que reciba una palabra (string) como parámetro y
#regrese un booleano (True / False) dependiendo si dicha palabra es un
#palíndromo.

def palindromo (palabra_ingresada = (input('¿Que palabras deseas verificar?: \n '))):   #se agrega la palabra por parte del usuario
    palabra_volteada = ((palabra_ingresada)[::-1])  #se invierte la palabra ingresada con el script [::-1] (lo investigue, pero tengo dudas de como funciona y porque).
    if palabra_ingresada == palabra_volteada:       #se compara la palabra original con la palabra "volteada"
        print(True)  #se imprime 'True' solo para hacernos saber que retorna el boolean requerido.
        print('¡Enhorabuena! Tu palabra es un palindromo')
        return (True)
    else:
        print(False) #se imprime 'False' solo para hacernos saber que retorna el boolean requerido.
        print('Tu palabra no es un palindromo, mamahuevo')
        return False
                                           
palindromo()        #se manda llamar la funcion