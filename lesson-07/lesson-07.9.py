n = int(input())
flag = 'NO'
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        flag = 'YES'
print(flag)