"""for i in range(9, 2, -2):
    print(i)
    # ke kanan
    #print(i, end=' ')

n = int(input('Masukkan angka anda='))
jum = 0
for i in range(n):
    i = i + 1
    jum = jum + i
    if i < n:
        print(i, end=' + ')
    else:
        print(i, " = ", jum)
        
i = 3
while i < 17:
    if i == 9:
        continue

    print(i)
    i += 3


n = int(input('Masukkan angka anda='))
jum = 0
i = 1
while (i <= n):
    jum = jum + i
    if i < n:
        print(i, end=' + ')
    else:
        print(i, " = ", jum)
    i = i + 1
"""

for a in range(1, 5):
    for b in range(1, 7):
        print(a*b, end='   ')
    print('  ')
