str_num = int(input())
words = []
for i in range(str_num):
    words.append(input())
word = input()
for i in words:
    if word.lower() in i.lower():
        print(i)
