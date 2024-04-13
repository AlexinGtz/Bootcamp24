
fullValuesList = input('Ingrese texto: \n')
searchedValue = input('Ingrese el valor buscado: \n')
# c = 0
# for i in fullValuesList:
#     if searchedValue == i:
#         c += 1
# print(f'El valor que estás buscando "{searchedValue}" se encuentra {c} veces.')


def search(searchedValue, fullValuesList):
    rep = 0
    for quantity in fullValuesList:
        if searchedValue == quantity:
            rep += 1
    return rep
repetition = search(searchedValue, fullValuesList)
print(f'El valor que estás buscando "{searchedValue}" se encuentra {repetition} veces.')


