import random

def ask_question(question):
    print(question)
    answer = input().lower().strip()
    if answer == 'больше':
        return 'больше'
    elif answer == 'меньше':
        return 'меньше'
    elif answer == 'равно':
        return 'равно'
    else:
        print('Что-то пошло не так')
        return ask_question(question)

def start_game():
    print('Добро пожаловать в игру "Загадай число"')
    attempts = 0
    print('Введите до какого числа вы загадывали?')
    max_num = input()
    if not max_num.isdigit():
        max_num = 100
    max_num = int(max_num)
    last_computer_num = max_num
    print('Загадайте число')
    while True:
        
        attempts += 1
        computer_num = last_computer_num // 2
        print(computer_num)
        answer = ask_question('Ваше число больше или меньше или равно?')
        if answer == 'больше':
            last_computer_num = max_num + computer_num
        elif answer == 'меньше':
            max_num = computer_num
            last_computer_num = max_num - computer_num
        else:
            print('Ура, я победил')
            break
start_game()
print('Спасибо за игру. Хотите сыграть еще(Да/Нет)?')
play_again = input()
if play_again.lower() == 'да':
    start_game()

