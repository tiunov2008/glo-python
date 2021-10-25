date = input().split('.')
if int(date[0]) * int(date[1]) == int(date[2]) % 100:
    print('True')
else:
    print('False')