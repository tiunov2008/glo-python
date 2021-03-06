import random
import jsonpickle
import os

def ask_question(question, rule):
    if rule == 'Да/Нет':
        while True:
            print(f'{question}, Нажмите Да или Нет')
            answer = input().lower().strip()
            if answer == 'да':
                return True
            elif answer == 'нет':
                return False
            else:
                print('Что-то пошло не так: ', end='')
    else:
        print(question)
        answer = input().strip()
        while True:
            if rule == 'digit':
                if not answer.isdigit():
                    print('Пожалуйста, введите число!')
                    answer = input().strip()
                else:
                    answer = int(answer)
                    break
            if rule == 'question':
                if answer[-1] != '?':
                    print('Пожалуйста, введите "?" в конце!')
                    answer = input().strip()
                elif len(answer) < 10:
                    print('Длина вопроса должна быть больше 10 символов!')
                    answer = input().strip()
                else:
                    break
        return answer


class Storage:
    def get(self, path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data
    
    def append(self, path, data):
        file = open(path, 'a')
        file.write(data)
        file.close()
    
    def writelines(self, path, data):
        file = open(path, 'w')
        data = file.writelines(data)
        file.close()
    
    def clear(self, path):
        file = open(path, 'w')
        file.write('')
        file.close()

    def write(self, path, data):
        file = open(path, 'w')
        file.write(data)
        file.close()
    
    def exists(self, path):
        return os.path.exists(path)

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuestionsStorage:
    def __init__(self):
        self.file_name = 'questions.json'
        self.questions = []
    def get_questions(self):
        if not storage.exists(self.file_name):
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
            self.update_question()
        
        data = storage.get(self.file_name)
        self.questions = jsonpickle.decode(data)
        return self.questions
    def add_question(self):
        question = ask_question('Введите вопрос', 'question')
        answer = ask_question('Введите ответ', 'digit')
        self.get_questions()
        self.questions.append(Question(question, answer))
        self.update_question()
        if ask_question('Хотите добавить ещё вопрос?', 'Да/Нет'):
            self.add_question()
    def remove_question(self):
        self.get_questions()
        while True:
            print('----------------------------')
            for i in range(len(self.questions)):
                print(i + 1, self.questions[i].text)
            print('----------------------------')
            print('Введите номера вопросов через пробел')
            questions = input().split(' ')
            print(sorted(questions, reverse=True))
            del_counter = 1
            for question in sorted(questions, reverse=True):
                question = int(question)
                if question < 0 or question > len(self.questions):
                    continue
                del self.questions[question - del_counter]
                del_counter +=1
            self.update_question()
            break
    def update_question(self):
        json_data = jsonpickle.encode(self.questions)
        storage.writelines(self.file_name, json_data)

    def get_right_answers(self):
        count_right_answers = 0
        for i in range(len(self.questions)):
            question_index = random.randint(0,len(self.questions) - 1)
            user_answer = ask_question('№ ' + str((i + 1)) + ' ' + self.questions[question_index].text, 'digit')
            right_answer = self.questions[question_index].answer
            if user_answer == right_answer:
                count_right_answers += 1
            self.questions.pop(question_index)
        return count_right_answers
    
class UsersResultStorage:
    def __init__(self): 
        self.file_name = 'db.json'
        self.results = []
    def get_results(self):
        if not storage.exists(self.file_name):
            storage.write(self.file_name, '[]')
        data = storage.get(self.file_name)
        self.results = jsonpickle.decode(data)
        return self.results
    def add_result(self, user):
        self.get_results()
        self.results.append(user)
        self.update_question()
    def update_question(self):
        json_data = jsonpickle.encode(self.results)
        storage.writelines(self.file_name, json_data)
    def show_results(self):
        self.get_results()
        print('Предыдущие результаты:')
        print(f'{"Имя":20} Кол-во правильных ответов {"Результат":12}')
        for i in self.results:
            print(f'{i.name:20} {str(i.count_right_answers):25} {str(i.result):12}\n', end='')
class User:
    def __init__(self, name, count_right_answers, result):
        self.name = name
        self.count_right_answers = count_right_answers
        self.result = result
    
    def get_result(self):
        results = ['Идиот','Кретин','Дурак','Нормальный','Талант','Гений']
        self.result = results[int(self.count_right_answers * (len(results) / self.result))]
        return self.result
    


#Функция начала теста
def start_test():
    print('Как вас зовут?')
    name = input()
    Questions = QuestionsStorage()
    questions = Questions.get_questions()
    len_questions = len(questions)
    count_right_answers = Questions.get_right_answers()
    user = User(name, count_right_answers, len_questions)
    print('Количество правильных ответов', name, '=', count_right_answers)
    print(name, user.get_result())
    users = UsersResultStorage()
    users.add_result(user)
    users.show_results()


    if ask_question('Хотите добавить вопрос?', 'Да/Нет'):
        Questions.add_question()
    if ask_question('Хотите удалить вопрос?', 'Да/Нет'):
        Questions.remove_question()
    if ask_question('Хотите пройти тест еще раз?', 'Да/Нет'):
        start_test()

#Запуск теста
storage = Storage()

jsonpickle.set_encoder_options('json', indent=4,
                                separators=(',', ':'),
                                ensure_ascii=False)

start_test()