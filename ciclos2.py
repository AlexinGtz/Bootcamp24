# break
# for i in range(40):
#     print(i)
#     if (i == 15):
#         break

# print('Afuera del ciclo')

# continue 
# for i in range(40):
#     if (i == 15):
#         continue
#     print(i)

# comentar ctrl + k ctrl + c
# descomentar ctrl + k ctrl + u

age = 20

isBaby = False

if(age < 3):
    isBaby = True

print(f'Es un bebe? {isBaby}')

# inline if / if de una linea

isABaby = True if age < 3 else False

print(f'Es un bebe? {isABaby}')

# or en datos

dbData = 'MAnuel'
userName = dbData or 'Anonimo'

print(userName)