def bisiesto(año):

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

año_usuario = int(input("Ingresa un año entre 1900 y 2030: "))

if bisiesto(año_usuario):
    print(f"{año_usuario} es un año bisiesto.")
else:
    print(f"{año_usuario} no es un año bisiesto.")