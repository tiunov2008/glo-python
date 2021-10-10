a = str(input())
b = str(input())
if ord(a) >= 97 and ord(a) <= 122 and ord(b) >= 97 and ord(b) <= 122:
    for i in range(min(ord(a), ord(b)), max(ord(a), ord(b))+1):
        print(chr(i))
else:
    print("Ошибка")
