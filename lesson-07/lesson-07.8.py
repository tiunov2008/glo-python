n = int(input())
num_max = 0
num_min = int(input())
for i in range(n-1):
    num = int(input())
    if num_max < num:
        num_max = num
    if num_min > num:
        num_min = num
print('Минимум равен', num_min)
print('Максимум равен',num_max)