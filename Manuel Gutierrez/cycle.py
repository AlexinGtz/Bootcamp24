name = str(input("¿Cuál es tu nombre?"))
print(f"Hola{name}")

cycle = int(input("Pon el último número que quieres en tu ciclo:   "))

if (cycle >= 101):
     print("Nel perro, ¿Porqué tanto?")
else:
    for cycleanswer in range (1,cycle+1):
         print(cycleanswer * cycleanswer)
print("el proceso ha terminado.")