import random

def is_valid(user_input , max_num):
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number >= 1 and user_number <= max_num:
            return True
        else:                
            return False
    else:
        return False

def start_game():
    print('Добро пожаловать в игру "Угадай число"')
    print('Введите до какого числа мне загадывать?')
    max_num = input()
    if not max_num.isdigit():
        max_num = 100
    max_num = int(max_num)
    secret_number = random.randint(1, max_num)
    attempts = 0

    while True:
        print('Введите число от 1 до', max_num)
        user_input = input()
        if not is_valid(user_input , max_num):
            continue
        user_number = int(user_input)
        attempts += 1
        if secret_number > user_number:
            print('Загаданное число больше, чем введенное вами')
        elif secret_number < user_number:
            print('Загаданное число меньше, чем введенное вами')
        else:
            print('УРА! Вы угадали число', '\nЧисло попыток:', attempts)
            break
start_game()
print('Спасибо за игру. Хотите сыграть еще(Да/Нет)?')
play_again = input()
if play_again.lower() == 'да':
    start_game()

