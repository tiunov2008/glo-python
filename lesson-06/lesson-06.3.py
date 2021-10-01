mes1 = input()
mes2 = input()
mes3 = input()
len_max = mes1
num_max = len(mes1)

if num_max < len(mes2):
    len_max = mes2
    num_max = len(mes2)
elif num_max == len(mes2):
    len_max += ', ' +  mes2
if num_max < len(mes3):
    len_max = mes3
    num_max = len(mes3)
elif num_max == len(mes3):
    len_max += ', ' + mes3

print(len_max)