import time
import random

class SafeQuestion:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

print('Bienvenido al juego del ahorcado donde debes de adivinar mi palabra secreta! ¿Cómo te llamas?')
name = str(input(''))
print ('¿Cuántos años tienes?')
age = int(input(''))

print("Hola " + name + ", vamos a jugar al ahorcado.")
print('Dejame pensar en una palabra mmmmm...')
time.sleep(3)
print ('Ya la tengo! Es algo dificil así que te daré 5 vidas')

questions = [
    SafeQuestion(
        'Vas conduciendo un camión, en la primera parada se suben 4 personas, en la segunda parada se baja 1 y se suben 6, en la tercera se bajan 4 y se suben 2 y en la ultima se suben 9. ¿Cuántos años tiene el conductor?',
        age),
    SafeQuestion('Cuantos lados tiene un triangulo', 3)
]

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
    lives = 1 
    redeemedLife = False

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

        questionanswer = ''
        
        if lives == 0:
            if redeemedLife:
                print('Nimodo, has perdido aun con la vida extra')
            else:
                print('Te doy una oportunidad para redimirte ¿quieres tomar el reto de una pregunta?')
                revive = str(input('si o no:   '))
                if revive == 'no' or redeemedLife:
                    print('La has cagado :\'c la palabra era ' + secretword)
                else:
                    chosenQuestion = random.choice(questions)
                    print (chosenQuestion.question)
                    questionanswer = int(input(''))
                    if questionanswer == chosenQuestion.answer:
                        lives += 1
                        redeemedLife = True
                        print('salvadota que te diste, ten una vida mi buen.')
                    else:
                        print("La has cagado :'c la palabra era "+ secretword)

play()
print("Gracias por jugar.")