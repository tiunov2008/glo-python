n = int(input())
total = 0
for i in range(n+1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        total += i
print(total)