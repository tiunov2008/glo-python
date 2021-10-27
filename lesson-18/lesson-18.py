import random
#Функция которая задает вопрос
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
#Функция начала теста
def start_test():
    questions = [
        'Сколько будет два плюс два умноженное на два?',
        'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?',
        'На двух руках 10 пальцев. Скоько пальцев на 5 руках?',
        'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
        'Пять свечей горело две потухли. Сколько свечей осталось?'
    ]
    count_right_answers = 0
    print('Как вас зовут?')
    name = input()
    for i in range(len(questions)):
        question_index = random.randint(0,len(questions))
        print('№', (i + 1), questions[question_index])

        user_answer = int(input())

        right_answer = answers[question_index]
        if user_answer == right_answer:
            count_right_answers += 1
        questions.pop(question_index)
    print('Количество правильных ответов', name, '=', count_right_answers)
    print(name, results[count_right_answers])
    if ask_question('Хотите пройти тест еще раз?'):
        start_test()
#Создание списков    
answers = [6, 9, 25, 60, 2]

results = ['Идиот','Кретин','Дурак','Нормальный','Талант','Гений']
#Запуск теста
start_test()