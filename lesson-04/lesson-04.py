print('Задание 1')
firstNum = int(input())
secondNum = int(input())
print(firstNum ** 2 + secondNum ** 2)


print('\nЗадание 2')
firstNum = int(input())
secondNum = int(input())
print(firstNum, 'умноженное на', secondNum, 'равно' , firstNum * secondNum)
print(firstNum, 'деленное  на', secondNum, 'равно' , firstNum / secondNum)
print(firstNum, 'нацело деленное на', secondNum, 'равно' , firstNum // secondNum)
print('Остаток от деления',firstNum, 'на', secondNum,  'равно' , firstNum % secondNum)
print(firstNum, 'в степени', secondNum, 'равно' , firstNum ** secondNum)

print('\nЗадание 3')
thirdNum = int(input())
if thirdNum > 0 and thirdNum // 1000 == 0:
    firstFigure = thirdNum // 100
    secondFigure = thirdNum // 10 % 10
    thirdFigure = thirdNum % 10
    print('Сумма цифр числа', thirdNum, 'равна' ,firstFigure + secondFigure + thirdFigure)
    print('Произведение цифр числа', thirdNum, 'равна' ,firstFigure * secondFigure * thirdFigure)
else:
    print('Ошибка')
    
print('\nЗадание 4')
r = int(input())
k = int(input())
n = int(input())
print('За', n ,'мяча нужно заплатить', r * n + k * n // 100,'рублей и', k * n % 100 ,'копеек')

print('\nЗадание 5')
thirdNum = int(input())
hours = thirdNum // 60 // 60
minutes = thirdNum // 60 - hours * 60
seconds = thirdNum - minutes * 60 - hours * 60 * 60
print(thirdNum ,' секунд - это ', hours  ,' час ', minutes ,' минут ', seconds,' сек')


print('\nЗадание 6')

thirdNum = int(input())
if thirdNum > 0 and thirdNum // 10000 == 0:
    firstFigure = thirdNum // 1000
    secondFigure = thirdNum // 100 % 10
    thirdFigure = thirdNum % 100 // 10
    fourthFigure = thirdNum % 10
    print(max(firstFigure, secondFigure, thirdFigure, fourthFigure))
else:
    print('Ошибка')

print('\nЗадание 7')
thirdNum = int(input())
if thirdNum < 1000000000:
    firstFigure = thirdNum // 100 % 10
    secondFigure = thirdNum // 10 % 10
    thirdFigure = thirdNum % 10
    print('Сумма цифр числа', thirdNum, 'равна' ,firstFigure + secondFigure + thirdFigure)
else:
    print('Ошибка')