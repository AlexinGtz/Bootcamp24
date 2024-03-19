rows = int(input("Enter the maximum height of the pyramid:   "))

for pyramid in range (rows):
    for pyramidup in range(pyramid + 1):
        print('A', end='')
    print()
for pyramid in range (rows):
    for pyramiddown in range(pyramid, rows-1):
        print('A', end='')
    print()