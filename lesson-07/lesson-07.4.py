a = int(input())
b = int(input())
for i in range(min(a, b), max(a, b)+1):
    if i % 2 == 0:
        print(i)