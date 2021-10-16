def max_elem(nums):
    max_num = 0
    for i in nums:
        if max_num < int(i):
            max_num = int(i)
    return int(max_num)
print(max_elem(input().split(' ')) * max_elem(input().split(' ')))