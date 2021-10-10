n = str(input())
if (ord(n) >= 97 and ord(n) <= 122) or (ord(n) >= 65 and ord(n) <= 90):
    print(n.swapcase())
else:
    print(n)