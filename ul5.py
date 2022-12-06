
"""
# versi for
for a in range(1, 5):
    j = 0
    for b in range(1, 7):
        j += a
        print(j, end='  ')
    print(' ')

# versi while
a = 1
while a <= 5:
    j = 0
    b = 1
    while b <= 7:
        j = j + a
        print(j, end='  ')
        b += 1
    print('')
    a += 1
"""
n = int(input("Masukkan jumlah anak ayam : "))
print("Tek kotek kotek kotek, anak ayam turun berkotek")
for i in range(n, 1, -1):
    print('anak ayam turunlah', i, 'mati satu tinggal', i-1)
print('anak ayam turunlah', i-1, 'mati satu tinggal induknya')

n = int(input("masukkan jumlah ayam :"))
print("si kotek kotek kotek")
i = 0
while i <= n:
    i += 1
    print('anak ayam turunlah', n, 'mati satu tinggal', n - 1)
    n -= 1

print('anak ayam turunlah ', n, 'mati satu tinggalah induknya')
