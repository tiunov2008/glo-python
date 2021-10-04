n = int(input())
num_max = 0
num_min = 9
while n != 0:
    if num_max < n % 10:
        num_max = n % 10
    if num_min > n % 10:
        num_min = n % 10
    n = n // 10
print('Минимум равен', num_min)
print('Максимум равен',num_max)