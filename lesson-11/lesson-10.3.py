adress = input()
nums_adress = adress.split('.')
flag = 'YES'
for i in nums_adress:
    if int(i) > 255 or int(i) < 0 or len(nums_adress) != 4:
        flag = 'NO'
    
print(flag)