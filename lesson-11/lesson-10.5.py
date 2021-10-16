nums = input().split(' ')
counter = ''
for a in range(len(nums)):
    flag = 'YES'
    for b in range(len(nums)):
        if nums[a] == nums[b] and a != b:
            flag = 'NO'
    if flag == 'YES':
        counter += nums[a] + ' '

print(counter)