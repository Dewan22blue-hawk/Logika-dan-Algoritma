nh = ["E", "D", "C", "B", "A"]
n = int(input("Masukkan angka dari 0-4: "))
print("Huruf dari Angka yang anda masukkan adalah ", nh[n])


kk = str(input('Masukkan kata/kalimat : '))
hk = int(input('Masukkan karakter ke: '))
print(len(kk))
print(kk[hk-1])
jk = len(kk)
for i in range(jk, 0, -1):
    print(kk[i-1], end='')
print(' ')

print()
