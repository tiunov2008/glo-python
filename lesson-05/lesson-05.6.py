num = int(input())
if num < 0 or num >= 36:
    print('Ошибка')
elif num == 0 :
    print('Зеленый')
elif num >= 1 and num <= 10:
    print('Черный')
elif num >= 11 and num <= 18:
    print('Красный')
elif num >= 19 and num <= 28:
    print('Черный')
elif num >= 29 and num <= 36:
    print('Красный')
