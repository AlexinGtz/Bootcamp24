
#pyramid height value set by user
Quantity_of_A = int(input('Pyramid height:  '))



#range top-down
for i in range(0, Quantity_of_A):
    print('A'* i)
#range bottom up inverted    
for i in range(Quantity_of_A, -1, -1):
    print('A'* i)
