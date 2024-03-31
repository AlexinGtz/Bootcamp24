

## se ingresara la operacion requerida por parte del cliente


while True:

    #('Porfavor, indique el primer valor:  ')
    operacion_requerida = int(input('Hola; Si deseas realizar cualquiera de estas operaciones, digita el numero que indica el menu:\n 1-Resta \n 2- Suman \n 3- Division \n 4- Mutiplicacion    \n  '))



    #print ( operacion_requerida)
    if operacion_requerida == 1: # SUMA
    #primer valor
        print('Porfavor digite el primer valor: ')
        primer_valor = int(input())

    #segundo valor
        print('Porfavor digite el segundo valor: ')
        segundo_valor = int(input())

        print('Su resultado es:', primer_valor + segundo_valor )

    elif operacion_requerida == 2: #RESTA
        print('Porfavor digite el primer valor: ')
        primer_valor = int(input())

    #segundo valor
        print('Porfavor digite el segundo valor: ')
        segundo_valor = int(input())

       
        print ('Su resultado es:', primer_valor - segundo_valor )
    
    elif operacion_requerida == 3: #DIVISION
        print('Porfavor digite el primer valor: ')
        primer_valor = int(input())

    #segundo valor
        print('Porfavor digite el segundo valor: ')
        segundo_valor = int(input())

        print ('Su resultado es:', primer_valor / segundo_valor )
    elif operacion_requerida == 4:  #MULTIPLICACION
        print('Porfavor digite el primer valor: ')
        primer_valor = int(input())

    #segundo valor
        print('Porfavor digite el segundo valor: ')
        segundo_valor = int(input())

        print ('Su resultado es:', primer_valor * segundo_valor )

    # si eligio otro valor diferente o quiere hacer otra operacion: ...     
    else:
        print('Intente otro valor del 1 al 4:')

 