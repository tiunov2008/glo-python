import random
import os

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
class UsersResultStorage:
    def save(self, user_data):
        file = open('./db.txt', 'a')
        file.write(f'{user_data.name:20} {str(user_data.count_right_answers):25} {str(user_data.result):12}\n')
        file.close()
    def get(self):
        file = open('./db.txt', 'r')
        results = file.readlines()
        print(f'{"Имя":20} Кол-во правильных ответов {"Результат":12}')
        for i in results:
            print(i, end='')
        file.close()
class User:
    def __init__(self, name, count_right_answers, result):
        self.name = name
        self.count_right_answers = count_right_answers
        self.result = result
    def get_result(self):
        results = ['Идиот','Кретин','Дурак','Нормальный','Талант','Гений']
        self.result = results[int(self.count_right_answers * (len(results) / self.result))]
        return self.result
class QuestionsStorage:
    def __init__(self):
        self.questions = []
    def get_questions(self):
        self.questions = []
        if not os.path.exists('question_db.txt'):
            self.questions = [
                Question('Сколько будет два делить на два умноженное на два?', 2),
                Question('Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 9),
                Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
                Question('Укол делают каждые полчаса, сколько нужно минут для трех уколов?', 60),
                Question('Пять свечей горело две потухли. Сколько свечей осталось?', 2),
                Question('Сколько месяцев в году имеют 28 дней?', 12),
                Question('С какой скоростью должна двигаться собака (в возможных для неё пределах), чтобы не слышать звона сковородки, привязанной к ее хвосту?', 0),
                Question('У квадратного стола отпилили один угол по прямой линии . Сколько теперь углов у стола?', 5)
            ]
        else:
            file = open('question_db.txt', 'r')
            results = file.readlines()
            file.close()
            for i in results:
                self.questions.append(Question(i.split('#')[0], int(i.split('#')[1])))
        return self.questions
    def add_question(self):
        print('Введите вопрос')
        question = input()
        print('Введите ответ')
        answer = input()
        while True:
            if not answer.isdigit():
                print('Пожалуйста, введите число!')
                answer = input()
            else:
                answer = int(answer)
                break
        self.get_questions()
        self.questions.append(Question(question, answer))
        self.update_question()
    def remove_question(self):
        self.get_questions()
        while True:
            print('Введите номер вопроса')
            print('\n')
            for i in range(len(self.questions)):
                print(i + 1, self.questions[i].text)
            question = int(input())
            if 0 > question > len(self.questions):
                continue
            self.questions.pop(question - 1)
            self.update_question()
            break
    def update_question(self):
        file = open('./question_db.txt', 'w')
        file.write('')
        file.close()
        file = open('./question_db.txt', 'a')
        for i in range(len(self.questions)):
            if i != len(self.questions):
                file.write(f'{self.questions[i].text}#{self.questions[i].answer}\n')
                continue
            file.write(f'{self.questions[i].text}#{self.questions[i].answer}')
        file.close()
    def get_right_answers(self):
        count_right_answers = 0
        for i in range(len(self.questions)):
            question_index = random.randint(0,len(self.questions) - 1)
            print('№', i + 1, self.questions[question_index].text)
            user_answer = input()
            while True:
                if not user_answer.isdigit():
                    print('Пожалуйста, введите число!')
                    user_answer = input()
                else:
                    user_answer = int(user_answer)
                    break
            right_answer = self.questions[question_index].answer
            if user_answer == right_answer:
                count_right_answers += 1
            self.questions.pop(question_index)
        return count_right_answers
    
#Функция которая задает вопрос
def ask_question(question):
    print(f'{question}, Нажмите Да или Нет')
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
    Questions = QuestionsStorage()
    questions = Questions.get_questions()
    len_questions = len(questions)
    print('Как вас зовут?')
    name = input()
    count_right_answers = Questions.get_right_answers()
    print('Количество правильных ответов', name, '=', count_right_answers)
    user = User(name, count_right_answers, len_questions)
    print(name, user.get_result())
    storage = UsersResultStorage()
    storage.save(user)
    print('Предыдущие результаты:')
    storage.get()
    if ask_question('Хотите добавить вопрос?'):
        Questions.add_question()
    if ask_question('Хотите удалить вопрос?'):
        Questions.remove_question()
    if ask_question('Хотите пройти тест еще раз?'):
        start_test()

#Запуск теста
start_test()