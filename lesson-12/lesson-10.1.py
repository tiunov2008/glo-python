def find_nums(num):
    total = 0
    while num != 0:
        num = num // 10
        total += 1 
    return total
print(find_nums(int(input())) * find_nums(int(input())))