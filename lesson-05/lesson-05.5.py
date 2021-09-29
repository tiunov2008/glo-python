k = int(input())
m = int(input())

if k % m != 0:
    print(k // m + 1)
else:
    print(k // m)
