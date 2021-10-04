total_plus = 0
total_minus = 0
n = 1
while n != 0:
    n = int(input())
    if n > 0:
        total_plus += 1
    if n < 0:
        total_minus += 1
print(total_plus * total_minus)