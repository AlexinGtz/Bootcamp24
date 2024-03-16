print('Bienvenido al juego del ahorcado donde debes de adivinar mi palabra secreta! ¿Cómo te llamas?')
name = str(input(''))
print ('¿Cuántos años tienes?')
age = int(input(''))
import time

print("Hola " + name + ", vamos a jugar al ahorcado.")
print('Dejame pensar en una palabra mmmmm...')
time.sleep(3)
print ('Ya la tengo! Es algo dificil así que te daré 5 vidas')

import random


question = 'Vas conduciendo un camión, en la primera parada se suben 4 personas, en la segunda parada se baja 1 y se suben 6, en la tercera se bajan 4 y se suben 2 y en la ultima se suben 9. ¿Cuántos años tiene el conductor? '

def getsecretword_random ():
    words = ['esternocleidomastoideo', name, 'ferrocarrilero', 'otorrinolaringologo', 'paralelepipedo', 'confianza', 'pendejo']
    randomword = random.choice(words)
    return randomword
def showtable (secretword,yourword):
    table=""
    for letter in secretword:
        if letter in yourword:
            table += letter
        else:
            table += "_"
    print(table)

def play():
    secretword = getsecretword_random()
    yourword = []
    lives = 5 

    while lives > 0:

        

        showtable(secretword,yourword)
        letter = input("Pon una letra: ")

        if letter in yourword:
            print("Ya pusiste esa wey.")
        
        if letter in secretword:
            yourword.append(letter)
            if set(yourword)==set(secretword):
                print('Ah perro te la rifaste te ganaste un pingüino ve a la tienda y compratelo :3')
                break
        else: 
            lives -= 1
            print(f'Chiale no jue te quedan {lives} para adivinar')
        
        if lives == 0:
            print('Te doy una oportunidad para redimirte ¿quieres tomar el reto de una pregunta?')
            revive = str(input('si o no:   '))  
            if revive == 'no':
                print('La has cagado :´c la palabra era '+ secretword)
            else:
                print (question)
                questionanswer = int(input(''))
            if questionanswer == age:
                lives += 1
                print('salvadota que te diste, ten una vida mi buen.')
            else:
                print('La has cagado :´c la palabra era '+ secretword)

    
play()