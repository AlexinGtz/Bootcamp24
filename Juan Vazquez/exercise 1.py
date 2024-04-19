#Se utiliza <while true> para que la app se ejecute todo el tiempo para mejor comodidad al probarla.
while True: 


# Se agrega valor a la variable principal "number_to_multiply"
   number_to_multiply = int(input("\n Hi! Please enter a number to get their square: "))

   number_to_multiply = number_to_multiply + 1


   if (number_to_multiply < 101):
      for i  in range(number_to_multiply):
         print(i * i) 
      print("Your squared value is:", i * i)  
            
   elif number_to_multiply > 100:
      print(" \n >>>>>>>Please try a lower number: ")
         
      



