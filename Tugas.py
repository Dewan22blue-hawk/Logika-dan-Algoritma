a = 700
t = 0
h = 0
for i in range(1, 5):
    t += 80
    h += 1
    print('Hari ke-', h, 'bisa melompat =', t)
for i in range(1, 4):
    t += 60
    h += 1
    print('Hari ke-', h, 'bisa melompat =', t)
while t <= 700:
    t += 30
    h += 1
    print('Hari ke-', h, 'bisa melompat =', t)
