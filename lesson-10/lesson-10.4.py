n = input()
if (ord(n) >= ord('a') and ord(n) <= ord('z')) or (ord(n) >= ord('A') and ord(n) <= ord('Z')):
    print(n.swapcase())
else:
    print(n)