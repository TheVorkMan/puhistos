import random

def hangman():
    words = ['python', 'program', 'hangman', 'game', 'player']  # Список слов для угадывания
    word = random.choice(words)  # Выбираем случайное слово из списка
    guessed_letters = []  # Угаданные буквы
    tries = 6  # Количество попыток

    while tries > 0:
        guessed_word = ''
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += '_'

        print(guessed_word)

        if guessed_word == word:
            print('Вы победили! Загаданное слово:', word)
            break

        guess = input('Введите букву: ').lower()

        if guess in guessed_letters:
            print('Вы уже угадывали эту букву.')
        elif guess in word:
            print('Правильно!')
            guessed_letters.append(guess)
        else:
            print('Неправильно!')
            tries -= 1

            if tries == 0:
                print('Вы проиграли! Загаданное слово:', word)
            else:
                print('Осталось попыток:', tries)

        print()

hangman()