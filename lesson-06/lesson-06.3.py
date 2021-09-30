mes1 = input()
mes2 = input()
mes3 = input()
if len(mes1) > len(mes2) and len(mes1) > len(mes3):
    print(mes1)
elif len(mes2) > len(mes3):
    print(mes2)
elif len(mes3) > len(mes2):
    print(mes3)
elif len(mes1) == len(mes2) and len(mes1) == len(mes3):
    print('Все статьи одинаковы по длине')