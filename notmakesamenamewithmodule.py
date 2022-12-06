wow = 8

for i in range(1, wow):
    for j in range(1, wow - i):
        print(' ', end='')
    for j in range(0, 2 * i - 1):
        print('*', end='')
    print()


for i in range(wow - 2, 0, -1):
    for j in range(1, wow - i):
        print(' ', end='')
    for j in range(1, 2 * i):
        print('*', end='')
    print()
