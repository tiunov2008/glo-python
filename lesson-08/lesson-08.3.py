a = int(input())
total = 0
b = a
while b != 0:
    total += b % 10
    b = b // 10    
if a % total != 0:
    print('NO')
else:
    print('YES')