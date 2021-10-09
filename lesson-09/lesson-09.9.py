n = int(input())
b = 0
while n // 10 != 0:
    b = n
    n = 0
    while b != 0:
        n += b % 10
        b = b // 10    
print(n)