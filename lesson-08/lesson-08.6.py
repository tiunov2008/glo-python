total_num = 0
total_symbols = 0
n = 1
while n != 0:
    n = int(input())
    total_num += n
    if n != 0:
        total_symbols += 1
print(total_num / total_symbols)