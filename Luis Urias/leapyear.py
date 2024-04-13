import calendar

LOWER_YEAR = 1900
UPPER_YEAR = 2030

# Definimos la función utilizando el método isleap de la biblioteca calendar
def leap_year(year):
    if (calendar.isleap(year)):
        return True
    else:
        return False

# ***** Opción 2 ***** haciendo la comparación del año según el múltiplo  
def leap_year2(year):
    if not year % 4 and (year % 100 or not year % 400):
        return True
    else:
        return False

while True:
    year = int(input(f"\nIntroduce un año entre {LOWER_YEAR} y {UPPER_YEAR}: "))
    
    # Validamos que sea un año entre los límites establecidos
    if (year >= LOWER_YEAR and year <= UPPER_YEAR):
        text = "sí" if leap_year2(year) else "no"
        print(f"\nEl año {year} {text} es bisiesto\n")
        break