year = int(input('Ingresa el año que desea saber: \n'))

def bisiesto(year):
    if year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 != 0: 
        return False
    else:
        print(f'{year} no es un dato válido.')
añoBisiesto = bisiesto(year)
if bisiesto(year):
    print(f'El año {year} sí es un año bisiesto.')
else:
    print(f'El año {year} no es un año bisiesto.')