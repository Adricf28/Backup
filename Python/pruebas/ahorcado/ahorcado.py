import random
from palabras import palabras
import string
from ahorcado_munieco import AHORCADO

def get_valid_word(palabras):
    word = random.choice(palabras)
    while '-' in word or ' ' in word:
        word = random.choice(palabras).strip()
    return word.upper()

def hangman():
    word = get_valid_word(palabras)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    wrong_letters = set()
    frase_final = True
    while len(word_letters) > 0:
        if len(used_letters) > 0:
            print('Has usado estas palabras: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Palabra: ', ' '.join(word_list))
        user_letters = input('Adivina una letra: ').upper()
        if user_letters == word:
            print(AHORCADO[len(wrong_letters)])
            break
        elif user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
                print(AHORCADO[len(wrong_letters)])
            else:
                wrong_letters.add(user_letters)
                try:
                    print(AHORCADO[len(wrong_letters)])
                except Exception:
                    frase_final = False
                    print('Ya has perdido, intentalo de nuevo.')
                    break
        elif user_letters in used_letters:
            print('Ya has usado esa letra, intentalo de nuevo.')
            print(AHORCADO[len(wrong_letters)])
        else:
            print(f'{(user_letters).lower().capitalize()} no es la palabra, sigue intentándolo.')
            wrong_letters.add(user_letters)
            try:
                print(AHORCADO[len(wrong_letters)])
            except Exception:
                frase_final = False
                print('Ya has perdido, intentalo de nuevo.')
                break
    if frase_final:
        print(f'Felicidades! Has acertado la palabra {word}')
    else:
        print(f'La palabra era {word}')
            
hangman()