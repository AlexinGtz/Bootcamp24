
# Definimos la función que contabiliza un valor dentro de un arreglo
def counter(values, value_to_count):
    # Utilizamos el método count  
    return values.count(value_to_count)

# ***** Opción 2 recorriendo el arreglo *****
def counter2(values, value_to_count):
    total = 0
    for i in range(0,len(values)):
        if values[i] == value_to_count:
            total += 1
    return total

values = [1,2,3,4,5,6,5,4,3,2,1,5,3,3]

print(counter(values,3))

print(counter2(values,6))

