import random
import re


def get_pictures():  # извлекает картинки из файла

    with open('pictures.txt', encoding='utf-8') as f:
        text = f.read()
        pictres = text.split(',')

    return pictres


def get_words(filename):  # принимает на вход файл со словами и возвращает список
    with open(filename, encoding='utf-8') as file:
        text = file.read()
        words = text.split(' ')
    return words


def choose_word(words):  # выбирает слово для отгадывания из списка
    i = random.randint(0, len(words) - 1)
    word = words[i]
    return word


def get_letter(passed_letters):  # заставляет игрока ввести букву верного формата
    letter = input('Введите букву: ')
    print()
    letter = letter.lower()
    while len(letter) != 1 or letter not in 'ёйцукенгшщзхъэждлорпавыфячсмитьбю' or letter in passed_letters:
        if len(letter) != 1:
            print('А это точно буква? Взгляните-ка: ', letter)
            letter = input('Введите новую букву: ')
        elif letter not in 'ёйцукенгшщзхъэждлорпавыфячсмитьбю':
            print('Это точно русская буква? Взгляните-ка:', letter)
            letter = input('Введите новую букву: ')
        elif letter in passed_letters:
            print('Что-то такое вы уже загадывали, давайте по-новой')
            letter = input('Введите новую букву: ')
    return letter


def word_meaning(word):  # считывает словарь и возвращает определение слова

    with open('dict.txt', encoding='utf-8') as f:
        text = f.read()
        word = word.upper()
        patt = r'\n' + word + r'\b' + r'.+?\n'
        result = re.findall(patt, text)
        for res in result:
            res.replace(r'\n', '')
        if len(result) == 0:
            result = ['К сожалению, в словаре не нашлось слова с данным значением :(']

    return result


def show_defenition(answ, word):  # в зависимости от желания пользователя демонстрирует определение
    if not answ:
        meaning = word_meaning(word)
        for mean in meaning:
            print(mean)
            print()


def screen_output(pictures, correct_letters, incorrect_letters, word):  # конфигурация на экране в данный момент времени
    print()
    print()
    print(pictures[len(incorrect_letters) - 1])  # высвечиваем виселицу
    print()

    print('Неправильные буквы:')  # через строку высвечиваем неправильные буквы
    for lett in incorrect_letters:
        print(lett, end=' ')
    print()
    print()

    s_hided_word = '_' * (len(word))
    hided_word = list(s_hided_word)  # создаем зашифрованное слово

    for s in range(len(word)):  # в зашифрованном слове открываем известные буквы
        if word[s] in correct_letters:
            hided_word[s] = word[s]

    for symbol in hided_word:  # печатаем известное слово
        print(symbol, end=' ')
    print()
    print()


def get_answer():  # получить ответ на вопрос да/нет
    print('[да/нет]')
    answ = input()
    return answ.lower().startswith('д')


print('_ВИСЕЛИЦА_' * 10)

filename = 'new_dict.txt'  # вводим рабочие значения
words = get_words(filename)
word = choose_word(words)
correct_letters = ''
incorrect_letters = ''
still_playing = True  # индикатор хода игры -- при проигрыше/выигрыше сменяется на False
pictures = get_pictures()
pictures.append('')

while still_playing:

    screen_output(pictures, correct_letters, incorrect_letters, word)  # выводим экранную конфигурацию

    letter = get_letter(incorrect_letters + correct_letters)  # ввод нужного формата

    if letter in word:
        correct_letters = correct_letters + letter

        found_all_letters = True
        for symbol in word:  # проверяем, есть ли неотгаданные буквы
            if symbol not in correct_letters:
                found_all_letters = False
                break

        if found_all_letters:
            print(word)
            print()
            print('Ура, вы победили!')
            print()
            print('Известно ли вам загаданное слово?')
            answ = get_answer()
            show_defenition(answ, word)
            still_playing = False

    else:
        incorrect_letters = incorrect_letters + letter

        if len(incorrect_letters) > len(pictures) - 1:
            print('Увы, ваши попытки закончились...')
            print()
            print('Было загадано слово', word)
            print()
            print('Известно ли вам загаданное слово?')
            answ = get_answer()
            show_defenition(answ, word)
            still_playing = False

    if not still_playing:
        print('Сыграть еще раз?')
        if get_answer():
            words = get_words(filename)
            word = choose_word(words)
            correct_letters = ''
            incorrect_letters = ''
            still_playing = True
        else:
            break
