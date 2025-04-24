limit = 400
for i in range(1, limit):
    n = i
    found = True
    steps = 0
    while(found):
        if n == 1:
            print(i, end = ' : ')
            print(steps)
            steps = 0
            found = False
        elif (n % 2) == 0:
            n = n/2
        else:
            n = (n*3) + 1
        steps += 1
