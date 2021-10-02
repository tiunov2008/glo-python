n = int(input())
flag = ''
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        if flag != 'NO':
            flag = 'YES'
    else:
        flag = 'NO'
print(flag)