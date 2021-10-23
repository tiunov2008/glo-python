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

def create_field():
    field = []
    for i in range(3):
        field.append(['*'] * 3)

    return field

def print_field(field):
    for i in range(3):
        for j in range(3):
            print(field[i][j], end = '')
        print()

def win(field):
    for i in range(3):
        if field[i][0] != '*' and field[i][0] == field[i][1] == field[i][2]:
            return True
    
    for i in range(3):
        if field[0][i] != '*' and field[0][i] == field[1][i] == field[2][i]:
            return True

    if field[0][0] != '*' and field[0][0] == field[1][1] == field[2][2]:
        return True

    if field[0][2] != '*' and field[0][2] == field[1][1] == field[2][0]:
        return True

    return False


def end_game(field):
    if win(field):
        return True
    
    for i in range(3):
        for j in range(3):
            if field[i][j] == '*':
                return False
    return True
def start_game():
    field = create_field()

    current_symbol = 'X'

    while not win(field):
        print_field(field)
        print('Ввидите номер строки и номер столбца')
        row = int(input())
        column = int(input())
        if not(row >= 1 and row <= 3) or not(column >= 1 and column <= 3):
            continue

        if field[row - 1][column - 1] != '*':
            continue
        
        field[row - 1][column - 1] = current_symbol

        if current_symbol == 'X':
            current_symbol = 'O'
        else:
            current_symbol = 'X'

    if current_symbol == 'X':
        print('Ура! Победил O')
        if ask_question('Хотите сыграть еще?'):
            start_game()
    else:
        print('Ура! Победил X')
        if ask_question('Хотите сыграть еще?'):
            start_game()

start_game()