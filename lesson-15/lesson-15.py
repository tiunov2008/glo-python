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
def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):

        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word
def get_user_word(secret_word):
    new_word = ''
    for i in range(len(secret_word)):
        new_word += '*'
    return new_word
def start():
    attemps = 0
    secret_word = 'троллейбус'
    user_word = get_user_word(secret_word)
    user_chars = ''
    question = 'Безрельсовое механическое транспортное средство, что это?'
    print('Вопрос: ',question)
    print(user_word)
    while user_word != secret_word:
        print('Введите букву')
        user_char = input().lower()
        if len(user_char) != 1 or not(ord(user_char) >= ord('а') and ord(user_char) <= ord('я')):
            continue
        if user_char in user_chars:
            print('Вы уже вводили эту букву')
            continue
        
        user_chars += user_char
        new_user_word = update_user_word(secret_word, user_word, user_char)
        if user_word == new_user_word:
            print('К сожелению, такой буквы нет в слове')
        else:
            print('Поздравляем, такая буква есть в слове')
        user_word = new_user_word
        attemps += 1

        print(user_word)
    print('Ура, вы угадали загаданное слово')
    print('Ваши попытки:', attemps)
    if ask_question('Сыграть еще раз?'):
        start()
start()