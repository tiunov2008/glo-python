a = int(input())
total = 0
while a != 0:
    if a % 10 == 5:
        total += 1  
    a = a // 10       
print(total)