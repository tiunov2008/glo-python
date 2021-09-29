num = int(input())
figure1 = num // 100000
figure2 = num // 10000 % 10
figure3 = num // 1000 % 10
figure4 = num // 100 % 10
figure5 = num // 10 % 10
figure6 = num % 10 
if num % 10000000 != 0:
    print('Ошибка')
elif(figure1 + figure2 + figure3 == figure4 + figure5 + figure6):
    print('Билет', num ,'счастливый')
elif(figure1 + figure2 + figure3 != figure4 + figure5 + figure6):
    print('Билет', num ,'НЕсчастливый')