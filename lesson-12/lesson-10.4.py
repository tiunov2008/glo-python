nums = int(input())
total = 0
for i in range(nums):
    if i != 0:
        total += 50
        continue
    total += 100
print(total)