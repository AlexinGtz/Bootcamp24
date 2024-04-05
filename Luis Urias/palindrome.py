
# Definimos la función donde se recibe una cadena de texto
def palindrome(text):
    # Colocamos el texto en reversa usando slide -1
    backward_text = text[::-1]
    if backward_text == text:
        return True
    else:
        return False
    
# ***** Opción 2 Recorriendo la cadena de texto *****
def palindrome2(text):
    for i in range(0,len(text)-1):
        # Comparamos los elementos en cada extremo
        if text[i] != text[len(text)-i-1]:
            return False
    return True


# Recibimos el texto, lo covertimos a minúsculas y le quitamos los espacios
text = input("\nEscribe la palabra o frase: ").lower().replace(" ", "")

print(palindrome(text))

print(palindrome2(text))
