email = input()
if '.' in email:
    if '@' in email:
        print('Корректный')
    else:
        print('Некорректный')
else:
    print('Некорректный')