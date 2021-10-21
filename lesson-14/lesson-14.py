import random
def is_digit(user_input):
    if user_input.isdigit():
        return True              
    else:
        return False
def generate_password(length, chars):
    password = ''
    for i in range(length):
        random_index = random.randint(0, len(chars) - 1)
        password += chars[random_index]
    return password
def ask_question(question, digit):
    if digit:
        print(question)
        answer = input().lower().strip()
        if answer.isdigit():
            return int(answer)
        else:
            print('Что-то пошло не так')
            return ask_question(question, True)
    else:
        print(question, ' Нажмите Да или Нет')
        answer = input().lower().strip()
        if answer == 'да':
            return True
        elif answer == 'нет':
            return False
        else:
            print('Что-то пошло не так')
            return ask_question(question, False)
def start():
    
    print('Привет. Я генератор паролей. Я задам пару уточняющих вопросов, на основе которых сгенерирую пароль. Давай начнем')
    length = ask_question('Введите длину пароля', True)
    pass_amount = ask_question('Введите количество паролей', True)

    enabled_chars = ''
    digits = '0123456789'
    latin_lowercase_letters = 'abcdefghijklmnopaqrstuvwxyz'
    latin_uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    russian_lowercase_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    russian_uppercase_letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuation = '!#$%&*+-=?@*'

    if ask_question('Включать ли цифры?', False):
        enabled_chars += digits
    if ask_question('Включать ли строчные латинские буквы?', False):
        enabled_chars += latin_lowercase_letters
    if ask_question('Включать ли заглавные латинские буквы?', False):
        enabled_chars += latin_uppercase_letters
    if ask_question('Включать ли строчные русские буквы?', False):
        enabled_chars += russian_lowercase_letters
    if ask_question('Включать ли заглавные русские буквы?', False):
        enabled_chars += russian_uppercase_letters
    if ask_question('Включать ли знаки пунктуации?', False):
        enabled_chars += punctuation
    if enabled_chars == '':
        print('Вы не выбрали не одного варианта')
    else:
        for i in range(pass_amount):
            print(generate_password(length, enabled_chars))
    if ask_question('Сгенерировать еще?', False):
        start()
start()