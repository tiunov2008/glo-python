n = 0
nums = ''
while True:
    n = int(input())
    if n >= 100:
        break
    elif n >= 10:
        nums += str(n) + '\n'
print(nums)