a = input()
last_char = ''
counter = 0
for i in a:
    if last_char == i:
        counter += 1 
    last_char = i
print(counter)