n = int(input())
flag = 'YES'
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        flag = 'NO'
print(flag)