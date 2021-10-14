a = input()
b = input()
if ord(a) >= ord('a') and ord(a) <= ord('z') and ord(b) >= ord('a') and ord(b) <= ord('z'):
    for i in range(min(ord(a), ord(b)), max(ord(a), ord(b))+1):
        print(chr(i))
else:
    print("Ошибка")
