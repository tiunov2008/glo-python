hour = 0
minutes = 0
seconds = 0
for i in range(0,24):
    hour = i
    for i in range(0,60):
        minutes = i
        for i in range(0,60):
            seconds = i
            print(hour, ':', minutes, ':', seconds)


