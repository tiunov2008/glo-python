n = int(input())
for i in range(1, n + 1):
    if i >= 2 and i <= 8:
        continue
    if i >= 128 and i <= 256:
        continue
    if i >= 1024 and i <= 1048:
        continue
    print(i)