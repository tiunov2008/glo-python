n = int(input())
total = 1
for i in range(n+1):
    if i % 10 == 2 or i % 10 == 9:
        total *= i
if(total == 1):
    print(0)
else:
    print(total)