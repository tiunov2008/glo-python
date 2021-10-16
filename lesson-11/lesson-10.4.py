nums = input().split(' ')
counter = 0
for a in range(len(nums)):
    for b in range(len(nums)):
        if nums[a] == nums[b] and a != b:
            counter += 1

print(counter // 2)