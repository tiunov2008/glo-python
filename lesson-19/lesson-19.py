import random
import math
#Функция для храннения данных
def save_db(name, count_right_answers, result):
    file = open('./db.txt', 'a')
    file.write(f'{name:20} {str(count_right_answers):25} {str(result):12}\n')
    file.close()
def get_db():
    file = open('./db.txt', 'r')
    results = file.readlines()
    print(f'{"Имя":20} Кол-во правильных ответов {"Результат":12}')
    for i in results:
        print(i, end='')
    file.close()
def get_result(count_right_answers, len_questions):
    results = ['Идиот','Кретин','Дурак','Нормальный','Талант','Гений']
    return results[int(count_right_answers * (len(results) / len_questions))]
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
        'Сколько будет два делить на два умноженное на два?',
        'Бревно нужно распилить на 10 частей, сколько надо сделать распилов?',
        'На двух руках 10 пальцев. Сколько пальцев на 5 руках?',
        'Укол делают каждые полчаса, сколько нужно минут для трех уколов?',
        'Пять свечей горело две потухли. Сколько свечей осталось?',
        'Сколько месяцев в году имеют 28 дней?',
        'С какой скоростью должна двигаться собака (в возможных для неё пределах), чтобы не слышать звона сковородки, привязанной к ее хвосту?',
        'У квадратного стола отпилили один угол по прямой линии . Сколько теперь углов у стола?'
    ]
    len_questions = len(questions)
    answers = [2, 9, 25, 60, 2, 12, 0, 5]
    count_right_answers = 0
    print('Как вас зовут?')
    name = input()
    for i in range(len(questions)):
        question_index = random.randint(0,len(questions) - 1)
        print('№', i + 1, questions[question_index])
        user_answer = input()
        while True:
            if not user_answer.isdigit():
                print('Пожалуйста, введите число!')
                user_answer = input()
            else:
                user_answer = int(user_answer)
                break
        right_answer = answers[question_index]
        if user_answer == right_answer:
            count_right_answers += 1
        questions.pop(question_index)
        answers.pop(question_index)
    print('Количество правильных ответов', name, '=', count_right_answers)
    print(name, get_result(count_right_answers, len_questions))
    save_db(name, count_right_answers, get_result(count_right_answers, len_questions))
    print('Предыдущие результаты:')
    get_db()
    if ask_question('Хотите пройти тест еще раз?'):
        start_test()



#Запуск теста
start_test()