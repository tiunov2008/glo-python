import random
def ask_question(question):
    print(question, ' Нажмите Да или Нет')
    answer = input().lower().strip()
    if answer == 'да':
        return True
    elif answer == 'нет':
        return False
    else:
        print('Что-то пошло не так')
        return ask_question(question)
def generate_secret_word():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_word = ''
    for i in range(4):
        random_index = random.randint(0, len(digits) - 1)
        secret_word += str(digits[random_index])
        digits.pop(random_index)
    return secret_word

def calculate_bulls_count(user_word, secret_word):
    сounter = 0
    for i in range(len(secret_word)):
        if secret_word[i] == user_word[i]:
            сounter += 1
    
    return сounter

def calculate_cows_count(user_word, secret_word):
    сounter = 0
    for i in range(len(user_word)):
        if secret_word[i] != user_word[i] and user_word[i] in secret_word:
            сounter += 1
    
    return сounter

secret_word = generate_secret_word()
while True:
    print('Найди число, задуманное компьютером!')
    user_word = input()
    if len(user_word) != len(secret_word) or not user_word.isdigit():
        print('Введите 4 числа без пробелов')
        continue
    flag = 'Yes'
    for a in range(len(user_word)):
        for b in range(len(user_word)):
            if user_word[a] == user_word[b] and a != b:
                flag = 'No'
                break
        break
    if flag == 'No':
        print('Числа не должны повторяться')
        continue
    bulls_count = calculate_bulls_count(user_word, secret_word)
    cows_count = calculate_cows_count(user_word, secret_word)
    print(bulls_count, 'быков', cows_count , 'коров' )

    if bulls_count == 4:
        print('УРА! Ты победил!')
        if ask_question('Хотите сыграть еще?'):
            secret_word = generate_secret_word()
        else:
            break
