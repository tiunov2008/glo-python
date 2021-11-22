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
            if rule == 'FIO':
                if answer.count(' ') != 2:
                    print('Пожалуйста, введите ФИО через пробелы')
                    answer = input().strip()
                elif len(answer) < 10:
                    print('Длина ФИО должна быть больше 10 символов!')
                    answer = input().strip()
                else:
                    break
            if rule == 'str':
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

class Student:
    def __init__(self, FIO, age, school_class):
        self.FIO = FIO
        self.age = age
        self.school_class = school_class

class School:
    def __init__(self, address, name, count_students):
        self.address = address
        self.name = name
        self.count_students = count_students

class SchoolStorage:
    def __init__(self, count_students):
        self.file_name = 'school.json'
        self.count_students = count_students
    def get_info(self):
        if not storage.exists(self.file_name):
            self.info = School('Новая Басманная ул., 4-6с4', 'Инженерная школа 1581', self.count_students)
            self.update_info()
        data = storage.get(self.file_name)
        self.info = jsonpickle.decode(data)
    def show_info(self):
        print(f'Название: {self.info.name}')
        print(f'Адрес: {self.info.address}')
        print(f'Колличество учеников: {self.info.count_students}')
    
    def change_info(self):
        self.info.name = ask_question('Введите название', 'str')
        self.info.address = ask_question('Введите адрес', 'str')
        self.update_info()

    def update_info(self):
        json_data = jsonpickle.encode(self.info)
        storage.writelines(self.file_name, json_data)

class StudentsStorage:
    def __init__(self):
        self.file_name = 'students.json'
        self.students = []

    def get_students(self):
        if not storage.exists(self.file_name):
            self.students = [
                Student('Андреев Артур Матвеевич', 7, 1),
                Student('Ершов Богдан Фёдорович', 8, 2),
                Student('Муратова Маргарита Васильевна',9 , 3),
                Student('Устинов Кирилл Ярославович', 13, 7),
                Student('Ильина Анна Ивановна', 12, 6),
                Student('Иванова Полина Артёмовна', 11, 5),
                Student('Гришина Валерия Матвеевна', 18, 11),
                Student('Соболев Александр Матвеевич', 15, 9)
            ]
            self.update_students()
        
        data = storage.get(self.file_name)
        self.students = jsonpickle.decode(data)


    def add_student(self):
        student = ask_question('Введите ФИО', 'FIO')
        age = ask_question('Введите возраст', 'digit')
        school_class = ask_question('Введите класс', 'digit')
        self.get_students()
        self.students.append(Student(student, age, school_class))
        self.update_students()
    def remove_student(self):
        self.get_students()
        print('----------------------------')
        for i in range(len(self.students)):
            print(i + 1, self.students[i].FIO)
        print('----------------------------')
        student = ask_question('Введите номер ученика', 'digit')
        while student >= len(self.students) or student <= 0:
            student = ask_question('Введите номер ученика', 'digit')
        self.students.pop(student - 1)
        self.update_students()
    def update_students(self):
        json_data = jsonpickle.encode(self.students)
        storage.writelines(self.file_name, json_data)

    def show_students(self):
        self.get_students()
        print('Предыдущие результаты:')
        print(f'{"  ФИО":35} {"Возраст":12} {"Класс":12}')
        b = 1
        for i in self.students:
            print(f'{str(b) + " " + i.FIO:35} {str(i.age):12} {str(i.school_class):12}\n', end='')    
            b += 1
    

def start_school():
    Students = StudentsStorage()
    Students.get_students()
    school = SchoolStorage(len(Students.students))
    school.get_info()

    if ask_question('Хотите получить информацию о школе?', 'Да/Нет'):
        school.show_info()
    if ask_question('Хотите изменить информацию о школе?', 'Да/Нет'):
        school.change_info()
    if ask_question('Хотите просмотреть учеников этой школы?', 'Да/Нет'):
        Students.show_students()
    if ask_question('Хотите добавить ученика?', 'Да/Нет'):
        Students.add_student()
    if ask_question('Хотите удалить ученика?', 'Да/Нет'):
        Students.remove_student()
    if ask_question('Еще раз?', 'Да/Нет'):
        start_school()


storage = Storage()

jsonpickle.set_encoder_options('json', indent=4,
                                separators=(',', ':'),
                                ensure_ascii=False)

start_school()
