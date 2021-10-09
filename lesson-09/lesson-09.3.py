n = int(input())
flag = 'NO'
for i in str(n):
    print(i)
    if i == '1':
        flag = 'YES'
        break
print(flag)
