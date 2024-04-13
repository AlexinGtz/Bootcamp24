nombre = 'hola mundo'

print(nombre)
nombreMayus = nombre.capitalize()
print(nombreMayus)
print(nombre)
print(nombreMayus)
resultado = nombre.find('alex')
print(resultado)

name = 'Alex'
lastName = 'Gutierrez'

fullName = name + ' ' + lastName
print(fullName)

hola = 'Hola'
print(hola * 4)

nombreProfesor = 'Manuel'
edadProfe = 23

saludo = 'Hola {}, tienes {} anios de edad'.format(nombreProfesor, edadProfe)
print(saludo)
nuevoSaludo = f'Hola {nombreProfesor}, tienes {edadProfe} anios de edad'
print(nuevoSaludo)

textoEnLinea = 'Hola, mundo'
textoEnLinea2 = 'Hola,\nmundo'
textoEnLinea3 = 'Hola,\tmundo'
textoEnLinea4 = 'Hola, alex\rmundo' 
textoEnLinea5 = 'Hola,\bmundo' 
print(textoEnLinea)
print(textoEnLinea2)
print(textoEnLinea3)
print(textoEnLinea4)
print(textoEnLinea5)

textoAyuda = 'Tienes que darle click el boton de \'Descarga\''
textoAyuda2 = "Tienes que darle click el boton de 'Descarga'"
textoAyuda3 = 'Tienes que darle click el boton de "Descarga"'
textoAyuda4 = "Tienes que darle click el boton de \"Descarga\""
textoAyuda5 = "Tienes que darle click el boton de \"Descarga\" o ir al enlace \\newEntry"
print(textoAyuda)
print(textoAyuda2)
print(textoAyuda3)
print(textoAyuda4)
print(textoAyuda5)

csv = '134l123l156l145l136l3457l34l25l235'
splittedCsv = csv.split('l')
print(splittedCsv)
nombresEstudiantes = 'Alex,Lucy,Rebeca,Juan'
splittedNames = nombresEstudiantes.split(',')
print(splittedNames)
africanName = "T`challa"
formatted2 = africanName.replace("`", "'")
print(formatted2)

removeStringOriginal = 'Hola Luis mundo'
indexToRemove = removeStringOriginal.find('Luis')
print(indexToRemove)
lengthOfString = len('Luis')
print(lengthOfString)
print(removeStringOriginal[1])
print(removeStringOriginal[0 : 5])
formattedString = removeStringOriginal[0:indexToRemove] + removeStringOriginal[(indexToRemove + lengthOfString + 1): ]
print(formattedString)

# Sets
conjuntoA = {1, 2 , 3, 4, 5, 6, 7, 8, 9, 10}
conjuntoB = {10, 20, 30, 40}

print(conjuntoA.union(conjuntoB))
print(conjuntoA.issuperset(conjuntoB))

for elemento in conjuntoA:
    print(elemento)

print('------------------------------------------------')

# Dict
usuariosLoggeado = {
    'nombre': 'Alex',
    'edad': 28,
    'nacionalidad': 'Mexicano',
    'ojos': 2
}

print(usuariosLoggeado['nombre'])

for key, value in usuariosLoggeado.items():
    print(key, value)